#!/usr/bin/node
exports.converter = function (base) { return snm => snm.toString(base); };
