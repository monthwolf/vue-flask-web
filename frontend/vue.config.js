/* eslint-disable prettier/prettier */
const webpack = require("webpack");
module.exports = {
  lintOnSave: false,
  publicPath: "./",
  // 跳过检查host
  devServer: {
    open: true,
    host: "127.0.0.1",
    historyApiFallback: true,
    allowedHosts: "all",
    proxy: {
      "/api": {
        target: "http://0.0.0.0:5000",
        pathRewrite: { "^/api": "" },
      },
      "/smms": {
        target: "https://sm.ms/api",
        pathRewrite: { "^/smms": "" },
        ws: true,
        changeOrigin: true,
        secure: false,
        Headers: {
          Referer: "https://smms.app",
        },
      },
      "/#/apidoc": {
        target: "http://0.0.0.0:5000",
        // pathRewrite: { "^/api": "" },
      },
    },
  },
  configureWebpack: {
    plugins: [
      new webpack.ProvidePlugin({
        $: "jquery",
        jQuery: "jquery",
        "windows.jQuery": "jquery",
      }),
    ],
  },
  chainWebpack: (config) => {
    config.module
      .rule("pug")
      .test(/\.pug$/)
      .use("pug-plain-loader")
      .loader("pug-plain-loader")
      .end();
  },
};
