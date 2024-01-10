#!/usr/bin/node
exports.esrever = function (list) {
  const newArr = [];
  while (list.length) {
    newArr.push(list.pop());
  }
  return newArr;
};
