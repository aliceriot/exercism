//
// This is only a SKELETON file for the 'Hello World' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

var HelloWorld = function(name) {
    if (name) {
        return 'Hello, ' + name + '!';
    } else {
        return 'Hello, World!';
    }
};

HelloWorld.prototype.hello = function(input) {
    HelloWorld(input);
};

module.exports = HelloWorld;
