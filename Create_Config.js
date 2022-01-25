
// JS Code - Run it in a Browser Console
// Create JSON-Config Template used for Program-Config
//
// Replace with your config, than run it in Browser Console
// Copy the Return
// Create in the Project main Folder a .config.json
// Place the Return there - Save
//
config = {}

config.newsletter = {} // Creates Sub Obj.
config.newsletter.url = ''
config.newsletter.cookie_list = ''
config.newsletter.boundary = ''
config.newsletter.pdf_endpoint = ''
config.newsletter.counter = ''
config.upload_targets.telegram = ''

console.log(JSON.stringify(config))