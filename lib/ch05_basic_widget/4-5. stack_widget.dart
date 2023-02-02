import 'package:flutterproject/ch05_basic_widget/4-2. column_widget.dart';
import 'package:flutterproject/ch05_basic_widget/4-4. expanded_widget.dart';
import 'package:flutterproject/ch05_basic_widget/2-5. gesture_detector_widget.dart';
import 'package:flutterproject/ch05_basic_widget/2-4. icon_button_widget.dart';
import 'package:flutterproject/ch05_basic_widget/2-2. outlined_button_widget.dart';
import 'package:flutterproject/ch05_basic_widget/3-3. padding_widget.dart';
import 'package:flutterproject/ch05_basic_widget/4-1. row_widget.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const StackWidgetExample());
}

class StackWidgetExample extends StatelessWidget {
  const StackWidgetExample({super.key});

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
