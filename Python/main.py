import asyncio
from aiosmtpd.controller import Controller

# Define your SMTP server class
class CustomSMTPServer:
    async def handle_DATA(self, server, session, envelope):
        # Called when a message is received
        print("onData:", envelope.content.decode())
        return '250 OK'

    async def handle_MAIL(self, server, session, envelope, address, mail_options):
        # Called when the sender (MAIL FROM) is received
        print("onMailFrom:", address, session.session)
        return '250 OK'

    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        # Called when the recipient (RCPT TO) is received
        print("onRcptTo:", address, session.session)
        return '250 OK'

    async def handle_CONNECT(self, server, session):
        # Called when a client connects
        print("onConnect:", session.session)
        return '220 Welcome to My SMTP Server'

# Create an instance of the controller and pass your server class
controller = Controller(CustomSMTPServer())

try:
    # Start the controller to run the server on port 25
    controller.start()
    print("Server is running on port 25")
    # Run the event loop
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    # Stop the controller if KeyboardInterrupt (Ctrl+C) is received
    controller.stop()
    print("Server stopped.")
