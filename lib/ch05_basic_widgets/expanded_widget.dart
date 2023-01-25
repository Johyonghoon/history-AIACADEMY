import 'package:flutterproject/ch05_basic_widgets/column_widget.dart';
import 'package:flutterproject/ch05_basic_widgets/gesture_detector_widget.dart';
import 'package:flutterproject/ch05_basic_widgets/icon_button_widget.dart';
import 'package:flutterproject/ch05_basic_widgets/outlined_button_widget.dart';
import 'package:flutterproject/ch05_basic_widgets/padding_widget.dart';
import 'package:flutterproject/ch05_basic_widgets/row_widget.dart';
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
