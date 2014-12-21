/**
 * Copyright 2013-present NightWorld.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


  var model = module.exports


/*
 * Required
 */

model.getAccessToken = function (bearerToken, callback) {
      console.log("getAccessToken:"+bearerToken)
      callback(null, {
        accessToken: "access_token",
        clientId: "101",
        expires: null,//1419155618000+300000,
        userId: "101"
      });

};

model.getClient = function (clientId, clientSecret, callback) {
        console.log("getClient")
      // This object will be exposed in req.oauth.client
      callback(null, {
        clientId: 101,
        clientSecret: "secret"
      });
};

model.getRefreshToken = function (bearerToken, callback) {
    console.log("getRefreshToken")
      callback(false, {"refresh_token":"","client_id":"","expires":3000,"user_id":101});
};

// This will very much depend on your setup, I wouldn't advise doing anything exactly like this but
// it gives an example of how to use the method to resrict certain grant types
var authorizedClientIds = ['abc1', 'def2'];
model.grantTypeAllowed = function (clientId, grantType, callback) {
    console.log("grantTypeAllowed")
  if (grantType === 'password') {
    return callback(false, authorizedClientIds.indexOf(clientId.toLowerCase()) >= 0);
  }

  callback(null, true);
};

model.saveAccessToken = function (accessToken, clientId, expires, userId, callback) {
    console.log("saveAccessToken")
 callback(null);
};

model.saveRefreshToken = function (refreshToken, clientId, expires, userId, callback) {
    console.log("saveRefreshToken")
      callback(null);
};

/*
 * Required to support password grant type
 */
model.getUser = function (username, password, callback) {
    console.log("getUser")
      callback(null, 101);

};