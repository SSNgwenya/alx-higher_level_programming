#!/usr/bin/node
// This function returns the reversed version of a list

exports.esrever = function (list) {
  const result = [...list];
  const length = result.length;

  for (let i = 0; i < Math.floor(length / 2); i++) {
    const temp = result[i];
    result[i] = result[length - 1 - i];
    result[length - 1 - i] = temp;
  }

  return result;
};
