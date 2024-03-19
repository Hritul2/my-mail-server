const SMTPServer = require("smtp-server").SMTPServer;
const port = 25;

const server = new SMTPServer({
  allowInsecureAuth: true,
  authOptional: true,
  onConnect(session, cb) {
    console.log(`onConnect`, session.id);
    cb(); // Accept the connection
  },
  onMailFrom(address, session, cb) {
    console.log(`onMailFrom`, address.address, session.id);
    cb();
  },
  onRcptTo(address, session, cb) {
    console.log(`onRcptTo`, address.address, session.id);
    cb();
  },
  onData(stream, session, cb) {
    let data = "";
    stream.on("data", (chunk) => {
      data += chunk.toString();
    });
    stream.on("end", () => {
      console.log(`onData:`, data);
      cb();
    });
    stream.on("error", (err) => {
      console.error("Stream error:", err);
      cb(err);
    });
  },
});

server.on("error", (err) => {
  console.error("Server error:", err);
});

server.listen(port, () => {
  console.log(`Server is running on port: ${port}`);
});
