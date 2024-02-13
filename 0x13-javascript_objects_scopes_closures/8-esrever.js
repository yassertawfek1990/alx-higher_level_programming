#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (sarry, scurrt) {
    sarry.push(scurrt);
    return sarry;
  }, []);
};
