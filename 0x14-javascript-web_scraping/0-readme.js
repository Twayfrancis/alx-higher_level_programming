#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

try {
  const fileContent = fs.readFileSync(filePath, 'utf8');
  console.log(fileContent);
} catch (error) {
  console.error(error);
}
