from python_framework import Controller, ControllerMethod, HttpStatus

from enumeration.AccessDomain import AccessDomain
import MessageDto


@Controller(url = '/message/emitter', tag='Message', description='Message controller')
class MessageController:

    @ControllerMethod(url = '/',
        apiKeyRequired = [AccessDomain.ADMIN],
        requestParamClass = [MessageDto.MessageQueryRequestDto],
        responseClass = [MessageDto.MessageCreationResponseDto]
        , logRequest = True
        , logResponse = True
    )
    def get(self, params=None):
        return self.service.message.findByQuery(params), HttpStatus.ACCEPTED

    @ControllerMethod(url = '/',
        apiKeyRequired = [AccessDomain.API, AccessDomain.USER, AccessDomain.ADMIN],
        requestClass = [MessageDto.MessageRequestDto],
        responseClass = [MessageDto.MessageCreationResponseDto]
        , logRequest = True
        , logResponse = True
    )
    def post(self, dto):
        return self.service.message.accept(dto), HttpStatus.ACCEPTED
