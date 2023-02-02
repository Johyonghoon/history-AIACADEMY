import 'package:flutterproject/ch05_basic_widget/2-5. gesture_detector_widget.dart';
import 'package:flutterproject/ch05_basic_widget/2-4. icon_button_widget.dart';
import 'package:flutterproject/ch05_basic_widget/2-2. outlined_button_widget.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const PaddingWidgetExample());
}

class PaddingWidgetExample extends StatelessWidget {
  const PaddingWidgetExample({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: Container(
              color: Colors.black,
              child: Container(
                color: Colors.blue,
                margin: const EdgeInsets.all(16.0),
                child: Padding(
                  // 상하, 좌우로 모두 16픽셀만큼 패딩을 적용합니다.
                  padding: const EdgeInsets.all(
                    16.0,
                  ),
                  child: Container(
                    color: Colors.red,
                    width: 50.0,
                    height: 50.0,
                  ),
                ),
              ),
          ),
        ),
      ),
    );
  }
}
