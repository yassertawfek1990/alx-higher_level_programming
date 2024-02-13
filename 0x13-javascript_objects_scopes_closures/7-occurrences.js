#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((scout, scurrt) => scurrt === searchElement ? scout + 1 : scout, 0);
};
