const express = require("express");
const bodyParser = require("body-parser");
var nodemailer = require("nodemailer");

const app = express();
const PORT = 3100;

// this application will receive JSON data
app.use(bodyParser.json());

// start the server on port 3100
app.listen(PORT, () => console.log(`Running on port ${PORT}`));

// process a GET request to http://localhost:3100/hello
app.get("/hello", (request, response) => {
  console.log(request.body);

  response.send("hi!");
});

app.post("/webhook", (request, response) => {
    const  event = request.body.event;
//   const activity = request.body.activity;
//   const msg = ` ${activity[0].fromAddress} `;

//   var transporter = nodemailer.createTransport({
//     service: "gmail",
//     auth: {
//       user: "ops@unifra.io",
//       pass: "Unifrayunying.2022",
//     },
//   });

//   var mailOptions = {
//     from: "ops@unifra.io",
//     to: "ops@unifra.io",
//     subject: "Update from unifra. You recieved a transaction!",
//     html: msg,
//   };

//   transporter.sendMail(mailOptions, function (error, info) {
//     if (error) {
//       console.log(error);
//     } else {
//       console.log("Email sent: " + info.response);
//     }
//   });
    console.log(request.body);
    response.send(event);
});