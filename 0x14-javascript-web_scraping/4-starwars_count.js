#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const wedgeAntillesId = 18;

const url = `${apiUrl}?characters=${wedgeAntillesId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movies = JSON.parse(body).results;
    const wedgeAntillesMovies = movies.filter((movie) => {
      return movie.characters.includes(wedgeAntillesId);
    });

    console.log(wedgeAntillesMovies.length);
  }
});
