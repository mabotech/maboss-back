
var koa = require('koa');
var oauthserver = require('koa-oauth-server');

var app = koa();

app.oauth = oauthserver({
  model:  require('./model'), // See https://github.com/thomseddon/node-oauth2-server for specification
  grants: ['password'],
  debug: true
});

app.use(app.oauth.authorise());

app.use(function *(next) {
  this.body = 'Secret area';
  yield next;
});


app.listen(6231);

