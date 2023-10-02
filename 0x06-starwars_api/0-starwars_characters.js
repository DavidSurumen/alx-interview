#!/usr/bin/node
/**
 * Script that prints all characters of a Star Wars movie. It takes
 * 1 command line arguement as Movie ID.
 *
 * Usage:
 *    ./0-starwars_characters.js [arguments]
 *
 * @author David Surumen
 */

const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, _, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
