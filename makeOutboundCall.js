const AWS = require("aws-sdk");
var connect = new AWS.Connect();

// main entry to the flow

exports.handler = (event, context, callback) => {
  //define parameter values to use in initiating the outbound call

  var params = {
    ContactFlowId: "",
    DestinationPhoneNumber: "",
    InstanceId: "",
    QueueId: "",
    Attributes: { Name: "Josh" },
    SourcePhoneNumber: "+",
  };

  // method used to initiate the outbound call from Amazon Connect

  console.log("Making outbound call to employee");

  connect.startOutboundVoiceContact(params, function (err, data) {
    if (err) console.log(err, err.stack);
    else console.log(data);
  });

  callback(null, event);
};
