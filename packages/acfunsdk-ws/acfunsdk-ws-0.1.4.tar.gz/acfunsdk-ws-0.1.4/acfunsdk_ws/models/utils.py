# coding=utf-8
import time
import json
import gzip
import proto
import base64
import filetype
from hashlib import md5
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from ..blackboxprotobuf import protobuf_to_json
from google.protobuf.json_format import MessageToJson
from google.protobuf.internal.python_message import GeneratedProtocolMessageType
from google.protobuf.internal.containers import RepeatedScalarFieldContainer
from google.protobuf.pyext._message import RepeatedScalarContainer
from dataclasses import dataclass
from .Im import PacketHeader_pb2, \
    UpstreamPayload_pb2, DownstreamPayload_pb2, \
    RegisterRequest_pb2, RegisterResponse_pb2, \
    ClientConfigGetRequest_pb2, ClientConfigGetResponse_pb2, \
    KeepAliveRequest_pb2, KeepAliveResponse_pb2, \
    GroupMemberListGetRequest_pb2, GroupMemberListGetResponse_pb2, \
    PullOldRequest_pb2, PullOldResponse_pb2, \
    SessionListResponse_pb2, SessionCreateRequest_pb2, \
    SessionCreateResponse_pb2, SessionRemoveRequest_pb2, \
    ErrorMessage_pb2, Message_pb2, Image_pb2
from .Live import ZtLiveCsCmd_pb2, \
    ZtLiveCsEnterRoom_pb2, ZtLiveCsHeartbeat_pb2, ZtLiveCsUserExit_pb2, \
    ZtLiveScMessage_pb2, acfun_live_pb2, \
    ZtLiveScActionSignal_pb2, \
    CommonActionSignalComment_pb2, CommonActionSignalLike_pb2, \
    CommonActionSignalUserEnterRoom_pb2, CommonActionSignalUserFollowAuthor_pb2, \
    CommonActionSignalGift_pb2, CommonActionSignalRichText_pb2, \
    ZtLiveScStateSignal_pb2, \
    CommonStateSignalDisplayInfo_pb2, CommonStateSignalTopUsers_pb2, \
    CommonStateSignalRecentComment_pb2, CommonStateSignalChatCall_pb2, \
    CommonStateSignalChatAccept_pb2, CommonStateSignalChatReady_pb2, \
    CommonStateSignalChatEnd_pb2, CommonStateSignalCurrentRedpackList_pb2, \
    CommonStateSignalAuthorChatCall_pb2, CommonStateSignalAuthorChatAccept_pb2, \
    CommonStateSignalAuthorChatReady_pb2, CommonStateSignalAuthorChatEnd_pb2, \
    CommonStateSignalAuthorChatChangeSoundConfig_pb2, \
    CommonStateSignalPKAccept_pb2, CommonStateSignalPKInvitation_pb2, \
    CommonStateSignalPKReady_pb2, CommonStateSignalPKSoundConfigChanged_pb2, \
    CommonStateSignalPkEnd_pb2, CommonStateSignalPkStatistic_pb2, \
    CommonStateSignalWishSheetCurrentState_pb2, \
    ZtLiveScNotifySignal_pb2, \
    CommonNotifySignalKickedOut_pb2, \
    CommonNotifySignalViolationAlert_pb2, \
    CommonNotifySignalLiveManagerState_pb2, \
    ZtLiveScStatusChanged_pb2, \
    ZtLiveScTicketInvalid_pb2

__author__ = 'dolacmeo'


def im_image_uploader(acer, to_uid: str, image_data: bytes) -> dict:
    md5_hex = md5(image_data).digest()
    head = {
        "Content-Type": filetype.guess_mime(image_data),
        "Content-MD5": base64.standard_b64encode(md5_hex),
        "file-type": filetype.guess_extension(image_data),
        "target": f"{to_uid}",
        "download-verify-type": "1",
    }
    param = {'kpn': "ACFUN_APP"}
    param = acer.update_token(param)
    post_req = acer.client.post("https://sixinpic.kuaishou.com/rest/v2/app/upload",
                                params=param, headers=head, data=image_data)
    return post_req.json()


def message_content_serialize(content: str):
    class MessageContent(proto.Message):
        content = proto.Field(proto.STRING, number=1)
    msg = MessageContent()
    msg.content = content.encode()
    return MessageContent.serialize(msg)


def proto_user_serialize(uid: int):
    class User(proto.Message):
        appId = proto.Field(proto.INT32, number=1)
        uid = proto.Field(proto.INT64, number=2)
    user = User()
    user.appId = 13
    user.uid = uid
    return User.serialize(user)


@dataclass(frozen=True)
class ProtosMap:
    command_rules = {
        "Basic.ClientConfigGet": ClientConfigGetResponse_pb2.ClientConfigGetResponse,
        "Basic.KeepAlive": KeepAliveResponse_pb2.KeepAliveResponse,
        "Message.Session": SessionListResponse_pb2.SessionListResponse,
        "Group.UserGroupList": GroupMemberListGetResponse_pb2.GroupMemberListGetResponse,
        "Message.PullOld": PullOldResponse_pb2.PullOldResponse,
        "Session.Create": SessionCreateResponse_pb2.SessionCreateResponse,
        "Message.Send": Message_pb2.Message,
        "Push.Message": Message_pb2.Message,
        "Message.SessionRemove": None,
        "Basic.Unregister": None,
    }
    live_acks = {
        "ZtLiveCsEnterRoomAck": ZtLiveCsEnterRoom_pb2.ZtLiveCsEnterRoomAck,
        "ZtLiveCsHeartbeatAck": ZtLiveCsHeartbeat_pb2.ZtLiveCsHeartbeatAck,
        "ZtLiveCsUserExitAck": ZtLiveCsUserExit_pb2.ZtLiveCsUserExitAck,
    }
    live_messages = {
        "ZtLiveScActionSignal": ZtLiveScActionSignal_pb2.ZtLiveScActionSignal,
        "ZtLiveScActionSignal.loader": {
            "CommonActionSignalComment": CommonActionSignalComment_pb2.CommonActionSignalComment,
            "CommonActionSignalLike": CommonActionSignalLike_pb2.CommonActionSignalLike,
            "CommonActionSignalUserEnterRoom": CommonActionSignalUserEnterRoom_pb2.CommonActionSignalUserEnterRoom,
            "CommonActionSignalUserFollowAuthor": CommonActionSignalUserFollowAuthor_pb2.CommonActionSignalUserFollowAuthor,
            "AcfunActionSignalThrowBanana": acfun_live_pb2.AcfunActionSignalThrowBanana,
            "CommonActionSignalGift": CommonActionSignalGift_pb2.CommonActionSignalGift,
            "CommonActionSignalRichText": CommonActionSignalRichText_pb2.CommonActionSignalRichText,
            "AcfunActionSignalJoinClub": acfun_live_pb2.AcfunActionSignalJoinClub,
        },
        "ZtLiveScStateSignal": ZtLiveScStateSignal_pb2.ZtLiveScStateSignal,
        "ZtLiveScStateSignal.loader": {
            "AcfunStateSignalDisplayInfo": acfun_live_pb2.AcfunStateSignalDisplayInfo,
            "CommonStateSignalDisplayInfo": CommonStateSignalDisplayInfo_pb2.CommonStateSignalDisplayInfo,
            "CommonStateSignalTopUsers": CommonStateSignalTopUsers_pb2.CommonStateSignalTopUsers,
            "CommonStateSignalRecentComment": CommonStateSignalRecentComment_pb2.CommonStateSignalRecentComment,
            "CommonStateSignalChatCall": CommonStateSignalChatCall_pb2.CommonStateSignalChatCall,
            "CommonStateSignalChatAccept": CommonStateSignalChatAccept_pb2.CommonStateSignalChatAccept,
            "CommonStateSignalChatReady": CommonStateSignalChatReady_pb2.CommonStateSignalChatReady,
            "CommonStateSignalChatEnd": CommonStateSignalChatEnd_pb2.CommonStateSignalChatEnd,
            "CommonStateSignalCurrentRedpackList": CommonStateSignalCurrentRedpackList_pb2.CommonStateSignalCurrentRedpackList,
            "CommonStateSignalAuthorChatCall": CommonStateSignalAuthorChatCall_pb2.CommonStateSignalAuthorChatCall,
            "CommonStateSignalAuthorChatAccept": CommonStateSignalAuthorChatAccept_pb2.CommonStateSignalAuthorChatAccept,
            "CommonStateSignalAuthorChatReady": CommonStateSignalAuthorChatReady_pb2.CommonStateSignalAuthorChatReady,
            "CommonStateSignalAuthorChatEnd": CommonStateSignalAuthorChatEnd_pb2.CommonStateSignalAuthorChatEnd,
            "CommonStateSignalAuthorChatChangeSoundConfig": CommonStateSignalAuthorChatChangeSoundConfig_pb2.CommonStateSignalAuthorChatChangeSoundConfig,
            "CommonStateSignalPKAccept": CommonStateSignalPKAccept_pb2.CommonStateSignalPKAccept,
            "CommonStateSignalPKInvitation": CommonStateSignalPKInvitation_pb2.CommonStateSignalPKInvitation,
            "CommonStateSignalPKReady": CommonStateSignalPKReady_pb2.CommonStateSignalPKReady,
            "CommonStateSignalPKSoundConfigChanged": CommonStateSignalPKSoundConfigChanged_pb2.CommonStateSignalPKSoundConfigChanged,
            "CommonStateSignalPkEnd": CommonStateSignalPkEnd_pb2.CommonStateSignalPkEnd,
            "CommonStateSignalPkStatistic": CommonStateSignalPkStatistic_pb2.CommonStateSignalPkStatistic,
            "CommonStateSignalWishSheetCurrentState": CommonStateSignalWishSheetCurrentState_pb2.CommonStateSignalWishSheetCurrentState,
        },
        "ZtLiveScNotifySignal": ZtLiveScNotifySignal_pb2.ZtLiveScNotifySignal,
        "ZtLiveScNotifySignal.loader": {
            "CommonNotifySignalKickedOut": CommonNotifySignalKickedOut_pb2.CommonNotifySignalKickedOut,
            "CommonNotifySignalViolationAlert": CommonNotifySignalViolationAlert_pb2.CommonNotifySignalViolationAlert,
            "CommonNotifySignalLiveManagerState": CommonNotifySignalLiveManagerState_pb2.CommonNotifySignalLiveManagerState,
        },
        "ZtLiveScStatusChanged": ZtLiveScStatusChanged_pb2.ZtLiveScStatusChanged,
        "ZtLiveScTicketInvalid": ZtLiveScTicketInvalid_pb2.ZtLiveScTicketInvalid,
    }


header_offset = 12
payload_offset = 16


class ProtosMaker:
    seqId = 0
    live_heartbeat = 0
    appId = 0
    instanceId = 0
    live_obj = None

    def __init__(self, acer, task_callback):
        self.acer = acer
        self.task = task_callback

    @staticmethod
    def aes_encrypt(key, payload):
        key = base64.standard_b64decode(key)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        payload = pad(payload, AES.block_size, 'pkcs7')
        result = cipher.encrypt(payload)
        return iv + result

    @staticmethod
    def aes_decrypt(key, data):
        key = base64.standard_b64decode(key)
        iv = data[:payload_offset]
        payload = data[payload_offset:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        result = cipher.decrypt(payload)
        return unpad(result, AES.block_size, 'pkcs7')

    def decode(self, message: bytes):
        # print(f"total length: {len(message)}")
        packet_header_len = int.from_bytes(message[4:8], byteorder='big')
        payload_len = int.from_bytes(message[8:12], byteorder='big')
        # print(f"packet_header_len: {packet_header_len} {message[4:8].hex()}")
        # print(f"payload_len: {payload_len} {message[8:12].hex()}")
        packet_header = PacketHeader_pb2.PacketHeader()
        header = message[header_offset:header_offset + packet_header_len]
        packet_header.ParseFromString(header)
        # print(packet_header)
        # print("=" * 40)
        payload_data = message[header_offset + packet_header_len:]
        # print(f"packet_header.encryptionMode: {packet_header.encryptionMode}")
        if packet_header.encryptionMode == 1:  # kEncryptionServiceToken
            decrypted_data = self.aes_decrypt(self.acer.tokens['ssecurity'], payload_data)
        elif packet_header.encryptionMode == 2:  # kEncryptionSessionKey
            decrypted_data = self.aes_decrypt(self.acer.tokens['sessKey'], payload_data)
        else:  # kEncryptionNone
            decrypted_data = payload_data
            stream_payload = ErrorMessage_pb2.ErrorMessage()
            stream_payload.ParseFromString(decrypted_data)
            print(stream_payload)
            raise BufferError(self.seqId, stream_payload.errorMessage)
        # decrypted_data = decrypted_data[:packet_header.decodedPayloadLen]
        # print(f"decrypted_data[{len(decrypted_data)}]: ", decrypted_data)
        # print(f"decrypted_data[b64]: {base64.standard_b64encode(decrypted_data)}")
        if self.seqId < 2:
            stream_payload = UpstreamPayload_pb2.UpstreamPayload()
        else:
            stream_payload = DownstreamPayload_pb2.DownstreamPayload()
        stream_payload.ParseFromString(decrypted_data)
        # print("#" * 40)
        # print(f"RecvCommand: {stream_payload.command}")
        # print("#" * 40)
        if stream_payload.errorCode:
            print(stream_payload)
            raise ValueError(f"[{stream_payload.errorCode}] {stream_payload.errorMsg}")
        command = stream_payload.command
        proto_class = ProtosMap.command_rules.get(command)
        if command == "Basic.Register":  # 初始化注册
            return self.BasicRegister_Response(packet_header, stream_payload)
        elif command == "Global.ZtLiveInteractive.CsCmd":  # 直播相关
            cmd_payload = ZtLiveCsCmd_pb2.ZtLiveCsCmdAck()
            cmd_payload.ParseFromString(stream_payload.payloadData)
            ack_type = cmd_payload.cmdAckType
            ack_payload = cmd_payload.payload
            if ack_type in ProtosMap.live_acks:
                return self.ZtLiveCsCmdAck_Response(ack_type, packet_header, ack_payload)
            if cmd_payload.errorCode:
                print(f"LiveError[{cmd_payload.errorCode}] {cmd_payload.errorMsg}")
        elif command == "Push.ZtLiveInteractive.Message":  # 直播推送
            live_push = ZtLiveScMessage_pb2.ZtLiveScMessage()
            live_push.ParseFromString(stream_payload.payloadData)
            msg_type = live_push.messageType
            msg_payload = gzip.decompress(live_push.payload) \
                if live_push.compressionType == 2 else live_push.payload
            if msg_type in ProtosMap.live_messages:
                return self.ZtLiveInteractive_Message(msg_type, packet_header, msg_payload)
            else:
                print(f"LiveMessageUnknown: {msg_type}\n{msg_payload}")
        elif proto_class is not None:  # 可解析消息
            return self.message_response(proto_class, packet_header, stream_payload)
        # 未知消息解析
        return self.unknown_response(packet_header, stream_payload)

    def BasicRegister_Response(self, packet_header, stream_payload):
        reg_resp = RegisterResponse_pb2.RegisterResponse()
        reg_resp.ParseFromString(stream_payload.payloadData)
        self.appId = packet_header.appId
        self.instanceId = packet_header.instanceId
        self.acer.tokens['sessKey'] = base64.standard_b64encode(reg_resp.sessKey)
        return packet_header.seqId, stream_payload.command, MessageToJson(reg_resp)

    def ZtLiveCsCmdAck_Response(self, ack_type, packet_header, ack_payload):
        if ack_type == "ZtLiveCsHeartbeatAck":
            self.task(*self.ZtLiveCsHeartbeat_Request())
        payload = ProtosMap.live_acks.get(ack_type)()
        payload.ParseFromString(ack_payload)
        return packet_header.seqId, f"LiveCmd.{ack_type}", json.loads(MessageToJson(payload))

    def ZtLiveInteractive_Message(self, msg_type, packet_header, msg_payload):
        self.task(*self.ZtLiveInteractiveMessage_Request())
        payload = ProtosMap.live_messages.get(msg_type)()
        payload.ParseFromString(msg_payload)
        those_msg = list()
        if msg_type in ["ZtLiveScActionSignal", "ZtLiveScStateSignal", "ZtLiveScNotifySignal"]:
            for item in payload.item:
                signal = item.signalType
                data = {"signal": f"{msg_type}.{signal}"}
                loader = ProtosMap.live_messages.get(f"{msg_type}.loader", {}).get(f"{signal}")
                if loader is not None:
                    loader = loader()
                    if isinstance(item.payload, (RepeatedScalarFieldContainer, RepeatedScalarContainer)):
                        data['payload'] = list()
                        for x in item.payload:
                            loader.ParseFromString(x)
                            data['payload'].append(json.loads(MessageToJson(loader)))
                    elif isinstance(item.payload, list):
                        data['payload'] = list()
                        for x in item.payload:
                            loader.ParseFromString(x)
                            data['payload'].append(json.loads(MessageToJson(loader)))
                    else:
                        loader.ParseFromString(item.payload)
                        data['payload'] = json.loads(MessageToJson(loader))
                those_msg.append(data)
        elif msg_type in ["ZtLiveScStatusChanged", "ZtLiveScTicketInvalid"]:
            those_msg = json.loads(MessageToJson(payload))
        else:
            those_msg = json.loads(MessageToJson(payload))
        if isinstance(those_msg, dict):
            those_msg = [those_msg]
        return packet_header.seqId, f"LivePush.{msg_type}", those_msg

    def message_response(self, proto_class, packet_header, stream_payload):
        payload = proto_class()
        payload.ParseFromString(stream_payload.payloadData)
        return packet_header.seqId, stream_payload.command, json.loads(MessageToJson(payload))

    def unknown_response(self, packet_header, stream_payload):
        message, typedef = protobuf_to_json(stream_payload.payloadData)
        if stream_payload.command not in ProtosMap.command_rules:
            print(f"[seqId:{packet_header.seqId}] {stream_payload.command}")
            print(typedef)
            print(message)
        payload_b64 = base64.standard_b64encode(stream_payload.payloadData)
        return packet_header.seqId, stream_payload.command, payload_b64

    def encode(self, key_n: int, command: str, payload, subBiz: [str, None] = None):
        self.seqId += 1
        # ####################   UpstreamPayload    ################# #
        upstream_payload = UpstreamPayload_pb2.UpstreamPayload()
        upstream_payload.command = command
        upstream_payload.seqId = self.seqId
        upstream_payload.retryCount = 1
        if hasattr(payload, "DESCRIPTOR"):  # protos_class has attr "DESCRIPTOR"
            upstream_payload.payloadData = payload.SerializeToString()
        elif isinstance(payload, bytes):
            upstream_payload.payloadData = payload
        if isinstance(subBiz, (str, bytes)):
            upstream_payload.subBiz = subBiz
        payload_body = upstream_payload.SerializeToString()
        # ####################      Encoding        ################# #
        token_info = PacketHeader_pb2.TokenInfo__pb2.TokenInfo()
        token_info.tokenType = 1
        if self.acer.is_logined:
            token_info.token = self.acer.tokens['api_st'].encode()
        else:
            token_info.token = self.acer.tokens['visitor_st'].encode()
        header = PacketHeader_pb2.PacketHeader()
        header.appId = self.appId
        header.instanceId = self.instanceId
        header.uid = self.acer.uid
        payload_len = len(payload_body)
        encrypted = payload_body
        if key_n in [1, 2]:
            key = self.acer.tokens['ssecurity'] if key_n == 1 else self.acer.tokens['sessKey']
            encrypted = self.aes_encrypt(key, payload_body)
        header.decodedPayloadLen = payload_len
        header.encryptionMode = key_n
        header.tokenInfo.CopyFrom(token_info)
        header.seqId = self.seqId
        header.kpn = b"ACFUN_APP"
        header_payload = header.SerializeToString()
        return self.seqId, command, b"".join([
            bytes.fromhex("abcd0001"),
            len(header_payload).to_bytes(4, "big"),
            len(encrypted).to_bytes(4, "big"),
            header_payload,
            encrypted
        ])

    def BasicRegister_Request(self):
        payload = RegisterRequest_pb2.RegisterRequest()
        app_info = RegisterRequest_pb2.AppInfo__pb2.AppInfo()
        app_info.sdkVersion = "kwai-acfun-live-link"
        app_info.linkVersion = "2.13.8"
        payload.appInfo.CopyFrom(app_info)
        device_info = RegisterRequest_pb2.DeviceInfo__pb2.DeviceInfo()
        device_info.platformType = 9
        device_info.deviceModel = "h5"
        device_info.deviceId = self.acer.did
        payload.deviceInfo.CopyFrom(device_info)
        payload.presenceStatus = 1
        payload.appActiveStatus = 1
        ztcommon_info = RegisterRequest_pb2.ZtCommonInfo__pb2.ZtCommonInfo()
        ztcommon_info.kpn = "ACFUN_APP"
        ztcommon_info.kpf = "PC_WEB"
        ztcommon_info.uid = self.acer.uid
        ztcommon_info.did = self.acer.did
        payload.instanceId = self.instanceId
        payload.ztCommonInfo.CopyFrom(ztcommon_info)
        return self.encode(1, "Basic.Register", payload, "mainApp")

    def ClientConfigGet_Request(self):
        payload = ClientConfigGetRequest_pb2.ClientConfigGetRequest()
        payload.version = 0
        return self.encode(2, "Basic.ClientConfigGet", payload)

    def KeepAlive_Request(self):
        payload = KeepAliveRequest_pb2.KeepAliveRequest()
        payload.presenceStatus = 1
        payload.appActiveStatus = 1
        payload.keepaliveIntervalSec = 120
        return self.encode(2, "Basic.KeepAlive", payload)

    def Unregister_Request(self):
        return self.encode(2, "Basic.Unregister", bytes())

    def BasicPing_Request(self):
        return self.encode(2, "Basic.Ping", bytes())

    def MessageSession_Request(self):
        return self.encode(2, "Message.Session", bytes([16, 0]))

    def SessionCreate_Request(self, target_uid: int):
        payload = SessionCreateRequest_pb2.SessionCreateRequest()
        chat = SessionCreateRequest_pb2.ChatTarget__pb2.ChatTarget()
        chat.targetId = f"{target_uid}"
        chat.targetType = 0
        payload.chatTarget.CopyFrom(chat)
        return self.encode(2, "Session.Create", payload)

    def SessionRemove_Request(self, target_uid: int):
        payload = SessionRemoveRequest_pb2.SessionRemoveRequest()
        payload.targetId = target_uid
        payload.strTargetId = f"{target_uid}"
        return self.encode(2, "Message.SessionRemove", payload)

    def UserGroupList_Request(self):
        payload = GroupMemberListGetRequest_pb2.GroupMemberListGetRequest()
        payload.groupId = b"0"
        sync_cookie_payload = GroupMemberListGetRequest_pb2.SyncCookie__pb2.SyncCookie()
        sync_cookie_payload.syncOffset = -1
        payload.syncCookie.CopyFrom(sync_cookie_payload)
        return self.encode(2, "Group.UserGroupList", payload)

    def MessagePullOld_Request(self, uid: int, minSeq: int, maxSeq: int, count: int = 10):
        payload = PullOldRequest_pb2.PullOldRequest()
        payload.target.ParseFromString(proto_user_serialize(uid))
        payload.minSeq = minSeq
        payload.maxSeq = maxSeq
        payload.count = count
        return self.encode(2, "Message.PullOld", payload)

    def Message_Request(self, target_uid: int, content: bytes, content_type: int = 0):
        payload = Message_pb2.Message()
        # payload.seqId = int(f"{time.time():.0f}{1:0>6}")
        payload.clientSeqId = int(f"{time.time():.0f}{1:0>6}")
        payload.timestampMs = int(f"{time.time():.0f}{1:0>3}")
        payload.fromUser.ParseFromString(proto_user_serialize(self.acer.uid))
        payload.targetId = target_uid
        payload.toUser.ParseFromString(proto_user_serialize(target_uid))
        payload.contentType = content_type
        payload.content = content
        payload.strTargetId = str(target_uid)
        return self.encode(2, "Message.Send", payload)

    def MessageContent_Request(self, target_uid: int, content: str):
        byte_content = message_content_serialize(content)
        return self.Message_Request(target_uid, byte_content, 0)

    def MessageImage_Request(self, target_uid: int, image_data: bytes):
        uploader_resp = im_image_uploader(self.acer, to_uid=f"{target_uid}", image_data=image_data)
        ks_uri = uploader_resp.get('uri')
        if ks_uri is None:
            print(uploader_resp)
            raise ValueError(uploader_resp['error_msg'])
        img_payload = Image_pb2.Image()
        img_payload.uri = ks_uri
        img_payload.width = 300
        img_payload.height = 300
        img_payload.contentLength = len(image_data)
        byte_content = img_payload.SerializeToString()
        return self.Message_Request(target_uid, byte_content, 1)

    def ZtLiveInteractive_CsCmd(self, cmd: str, cmd_payload):
        if self.live_obj is None:
            raise ValueError(f"Need Enter Live Rome First!!!\nUSE: ZtLiveCsEnterRoom_Request(uid)")
        payload = ZtLiveCsCmd_pb2.ZtLiveCsCmd()
        payload.cmdType = cmd
        payload.payload = cmd_payload.SerializeToString()
        payload.liveId = self.live_obj.liveId
        payload.ticket = self.live_obj.availableTickets[0]
        return self.encode(2, "Global.ZtLiveInteractive.CsCmd", payload, "mainApp")

    def ZtLiveCsEnterRoom_Request(self, live_obj):
        self.live_obj = live_obj
        enter_room_payload = ZtLiveCsEnterRoom_pb2.ZtLiveCsEnterRoom()
        enter_room_payload.isAuthor = self.acer.uid == live_obj.uid
        # enter_room_payload.reconnectCount = 0
        # enter_room_payload.lastErrorCode = 0
        enter_room_payload.enterRoomAttach = live_obj.enterRoomAttach
        enter_room_payload.clientLiveSdkVersion = "kwai-acfun-live-link"
        return self.ZtLiveInteractive_CsCmd("ZtLiveCsEnterRoom", enter_room_payload)

    def ZtLiveCsHeartbeat_Request(self):
        self.task(*self.ZtLiveInteractiveMessage_Request())
        self.live_heartbeat += 1
        if self.live_heartbeat % 5 == 4:
            # 即启动Heartbeat定时器后每50秒，发送KeepAliveRequest，SeqId + 1
            self.task(*self.KeepAlive_Request())
        time.sleep(4)
        heartbeat_payload = ZtLiveCsHeartbeat_pb2.ZtLiveCsHeartbeat()
        heartbeat_payload.clientTimestampMs = int(time.time()) * 1000
        heartbeat_payload.sequence = self.live_heartbeat
        return self.ZtLiveInteractive_CsCmd("ZtLiveCsHeartbeat", heartbeat_payload)

    def ZtLiveInteractiveMessage_Request(self):
        return self.encode(2, "Push.ZtLiveInteractive.Message", bytes(), "mainApp")
