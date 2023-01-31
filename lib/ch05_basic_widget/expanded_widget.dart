import 'package:flutterproject/ch05_basic_widget/column_widget.dart';
import 'package:flutterproject/ch05_basic_widget/gesture_detector_widget.dart';
import 'package:flutterproject/ch05_basic_widget/icon_button_widget.dart';
import 'package:flutterproject/ch05_basic_widget/outlined_button_widget.dart';
import 'package:flutterproject/ch05_basic_widget/padding_widget.dart';
import 'package:flutterproject/ch05_basic_widget/row_widget.dart';
import 'package:flutter/material.dart';

class ExpandedWidgetExample extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: Column(
            children: [
              Expanded(
                child: Container(
                  color: Colors.blue,
                ),
              ),
              Expanded(
                child: Container(
                  color: Colors.red,
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
