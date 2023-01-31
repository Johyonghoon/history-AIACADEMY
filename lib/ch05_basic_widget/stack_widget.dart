import 'package:flutterproject/ch05_basic_widget/column_widget.dart';
import 'package:flutterproject/ch05_basic_widget/expanded_widget.dart';
import 'package:flutterproject/ch05_basic_widget/gesture_detector_widget.dart';
import 'package:flutterproject/ch05_basic_widget/icon_button_widget.dart';
import 'package:flutterproject/ch05_basic_widget/outlined_button_widget.dart';
import 'package:flutterproject/ch05_basic_widget/padding_widget.dart';
import 'package:flutterproject/ch05_basic_widget/row_widget.dart';
import 'package:flutter/material.dart';

class StackWidgetExample extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: Stack(
            children: [
              Container(
                height: 300.0,
                width: 300.0,
                color: Colors.red,
              ),
              Container(
                height: 250.0,
                width: 250.0,
                color: Colors.yellow,
              ),
              Container(
                height: 200.0,
                width: 200.0,
                color: Colors.blue,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
