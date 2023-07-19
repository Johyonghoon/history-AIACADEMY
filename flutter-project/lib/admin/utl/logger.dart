import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';

class Logger {
  static void showToast(String message){
    Fluttertoast.showToast(msg: message,
    backgroundColor: Colors.white,
    toastLength: Toast.LENGTH_LONG,
    gravity: ToastGravity.BOTTOM);
  }
}