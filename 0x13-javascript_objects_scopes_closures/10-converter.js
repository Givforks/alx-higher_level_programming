#!/usr/bin/node
#converter
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
