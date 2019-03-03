const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;
const notifyServiceSid = process.env.NOTIFY_SERVICE_SID;

const client = require('twilio')(accountSid, authToken);

const fs = require('fs');

if (!fs.existsSync('numbers.txt')) {
	console.log('No file named numbers.txt in working directory');
	console.log('Please, create a list of numbers in the format: +10000000000');
	process.exit(1);
	
}

if (!fs.existsSync('body.txt')) {
	console.log('Please include a body.txt file');
	process.exit(1);
	
}

// Load numbers
var numbers = fs.readFileSync('numbers.txt', 'utf8').split("\n").filter(function(el) {
	return el != '';});
// Load body text
var bodyText = fs.readFileSync('body.txt', 'utf8');

const bindings = numbers.map(number => {
  return JSON.stringify({ binding_type: 'sms', address: number });
});

client.notify.services(notifyServiceSid)
  .notifications.create({
	toBinding: bindings,
    body: bodyText
  })
  .then(notification => console.log(notification.sid))
  .catch(error => console.log(error));
