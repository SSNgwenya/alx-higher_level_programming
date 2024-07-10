#!/usr/bin/node
// This script imports an array and computes a new array

const { list } = require('./100-data');
const transformedList = list.map((value, index) => value * index);
console.log('Original list:', list);
console.log('Transformed list:', transformedList);
