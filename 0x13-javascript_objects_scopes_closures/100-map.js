#!/usr/bin/node
// This script imports an array and computes a new array

const { list } = require('./100-data.js');

const newList = list.map((value, index) => value * index);
console.log(list);
console.log(newList);
