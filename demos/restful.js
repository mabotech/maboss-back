
var http = require('http');

var koa = require('koa')
  ,mount = require('koa-mount')
  , Router  = require('koa-router');

function findOne (id){

return '{id:"id1", name:"name1"}'
    
}

var app = koa();

var APIv1 = new Router();
var APIv2 = new Router();

APIv1.get('/sign-in', function *() {
  // ...
    console.log("v1 get")
    this.set('X-Response-Time', 4 + 'ms');
    this.set('allow', 'GET,HEAD,POST,OPTIONS');
    this.set('Content-Type','application/json; charset=UTF-8');
    this.body = '{"type":"get"}'
});

APIv2.post('/sign-in', function *() {
  // ...
    console.log("v2 post")
    this.body = "post"
});

APIv2.put('/sign-in', function *() {
  // ...
    console.log("v2 put")
    this.body = "put"
});

APIv2.patch('/sign-in', function *() {
  // ...
    console.log("v2 patch")
     this.body = "patch"
});

APIv2.head('/sign-in', function *() {
  // ...
    console.log("v2 head")
    this.set('x-ratelimit-remaining', '4995')
    this.set('x-ratelimit-limit', '5000')
    //this.body = "head"
});

APIv2.options('/sign-in', function *() {
  // ...
    console.log("v2 optios")
    this.body = "options"
});

APIv2.delete('/sign-in', function *() {
  // ...
    console.log("v2 delete")
    this.body = "delete"
});

app
  .use(mount('/v1', APIv1.middleware()))
  .use(mount('/v2', APIv2.middleware()));

http.createServer(app.callback()).listen(6230);
console.log("listen on port: 6230")