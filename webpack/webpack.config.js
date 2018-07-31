// const nodeExternals = require('webpack-node-externals');
const path = require('path');
// const webpack = require('webpack');

module.exports = {
  entry: path.resolve(__dirname, '..', 'frontend', 'src', 'main.js'),
  
  target: 'web',
  
  mode: 'development',
  
  output: {
    path: path.resolve(__dirname, '..', 'frontend', 'public', 'dist'),
    filename: 'bundle.js'
  },

  module: {
    rules: [
      { test: /\.js$/, exclude: /node_modules/, loader: "babel-loader" }
    ]
  },

  /*externals: [
    nodeExternals({
    }), // in order to ignore all modules in node_modules folder
  ],*/

  devtool: 'source-map'
};