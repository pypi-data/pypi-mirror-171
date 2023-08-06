(function webpackUniversalModuleDefinition(root, factory) {
	if(typeof exports === 'object' && typeof module === 'object')
		module.exports = factory();
	else if(typeof define === 'function' && define.amd)
		define([], factory);
	else if(typeof exports === 'object')
		exports["trame_tauri"] = factory();
	else
		root["trame_tauri"] = factory();
})((typeof self !== 'undefined' ? self : this), function() {
return /******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "fae3");
/******/ })
/************************************************************************/
/******/ ({

/***/ "fae3":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
// ESM COMPAT FLAG
__webpack_require__.r(__webpack_exports__);

// EXPORTS
__webpack_require__.d(__webpack_exports__, "install", function() { return /* reexport */ install; });

// CONCATENATED MODULE: ./node_modules/@vue/cli-service/lib/commands/build/setPublicPath.js
// This file is imported into lib/wc client bundles.

if (typeof window !== 'undefined') {
  var currentScript = window.document.currentScript
  if (false) { var getCurrentScript; }

  var src = currentScript && currentScript.src.match(/(.+\/)[^/]+\.js(\?.*)?$/)
  if (src) {
    __webpack_require__.p = src[1] // eslint-disable-line
  }
}

// Indicate to webpack that this file can be concatenated
/* harmony default export */ var setPublicPath = (null);

// CONCATENATED MODULE: ./src/components/index.js
/* harmony default export */ var components = ({});
// CONCATENATED MODULE: ./src/utils/tauri/clipboard.js
function readText() {
  return window.__TAURI__.clipboard.readText();
}
function writeText(txt) {
  return window.__TAURI__.clipboard.writeText(txt);
}
/* harmony default export */ var clipboard = ({
  readText,
  writeText
});
// CONCATENATED MODULE: ./src/utils/tauri/dialog.js
function ask(message, options) {
  return window.__TAURI__.dialog.ask(message, options);
}
function dialog_confirm(message, options) {
  return window.__TAURI__.dialog.confirm(message, options);
}
function dialog_open(options) {
  return window.__TAURI__.dialog.open(options);
}
function save(options) {
  return window.__TAURI__.dialog.save(options);
}
/* harmony default export */ var dialog = ({
  ask,
  confirm: dialog_confirm,
  open: dialog_open,
  save
});
// CONCATENATED MODULE: ./src/utils/tauri/event.js
function emit(event, payload) {
  return window.__TAURI__.event.emit(event, payload);
}
function listen(event, handler) {
  return window.__TAURI__.event.listen(event, handler);
}
function once(event, handler) {
  return window.__TAURI__.event.once(event, handler);
}
/* harmony default export */ var tauri_event = ({
  emit,
  listen,
  once
});
// CONCATENATED MODULE: ./src/utils/tauri/globalShortcut.js
function isRegistered(shortcut) {
  return window.__TAURI__.globalShortcut.isRegistered(shortcut);
}
function register(shortcut, handler) {
  return window.__TAURI__.globalShortcut.register(shortcut, handler);
}
function registerAll(shortcuts, handler) {
  return window.__TAURI__.globalShortcut.registerAll(shortcuts, handler);
}
function unregister(shortcut) {
  return window.__TAURI__.globalShortcut.unregister(shortcut);
}
function unregisterAll() {
  return window.__TAURI__.globalShortcut.unregisterAll();
}
/* harmony default export */ var globalShortcut = ({
  isRegistered,
  register,
  registerAll,
  unregister,
  unregisterAll
});
// CONCATENATED MODULE: ./src/utils/tauri/notification.js
function isPermissionGranted() {
  return window.__TAURI__.globalShortcut.isPermissionGranted();
}
function requestPermission() {
  return window.__TAURI__.globalShortcut.requestPermission();
}
function sendNotification(options) {
  return window.__TAURI__.globalShortcut.sendNotification(options);
}
/* harmony default export */ var notification = ({
  isPermissionGranted,
  requestPermission,
  sendNotification
});
// CONCATENATED MODULE: ./src/utils/tauri/tauri.js
function invoke(cmd, args) {
  return window.__TAURI__.tauri.invoke(cmd, args);
}
function transformCallback(fn, once = false) {
  return window.__TAURI__.tauri.transformCallback(fn, once);
}
/* harmony default export */ var tauri = ({
  invoke,
  transformCallback
});
// CONCATENATED MODULE: ./src/utils/tauri/index.js






/* harmony default export */ var utils_tauri = ({
  clipboard: clipboard,
  dialog: dialog,
  event: tauri_event,
  globalShortcut: globalShortcut,
  notification: notification,
  tauri: tauri
});
// CONCATENATED MODULE: ./src/utils/index.js

/* harmony default export */ var utils = ({
  tauri: utils_tauri
});
// CONCATENATED MODULE: ./src/use.js


function install(Vue) {
  Object.keys(components).forEach(name => {
    Vue.component(name, components[name]);
  });

  // Extend trame.utils
  Object.assign(window.trame.utils, utils);
}
// CONCATENATED MODULE: ./node_modules/@vue/cli-service/lib/commands/build/entry-lib-no-default.js




/***/ })

/******/ });
});
//# sourceMappingURL=vue-trame_tauri.umd.js.map