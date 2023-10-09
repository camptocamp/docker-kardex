#!/usr/bin/python3
import asyncio


async def handle_kardex(reader, writer):
    while True:
        data = await reader.readline()
        data = data.replace(b'\0', b'')
        if not data:
            return
        message = data.decode()
        addr = writer.get_extra_info('peername')

        print("Received {!r} from {!r}".format(message, addr))
        code, sep, endmsg = message.partition('|')
        answer = '0' + sep + endmsg
        print("Send: %r" % answer)
        writer.write(answer.encode('iso-8859-1', 'replace'))


def main():
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handle_kardex, '0.0.0.0', 9600, loop=loop)
    server = loop.run_until_complete(coro)
    addr = server.sockets[0].getsockname()
    print('Serving on {!r}'.format(addr))

    loop.run_forever()


if __name__ == '__main__':
    print("[Start] kardex Sim")
    main()
