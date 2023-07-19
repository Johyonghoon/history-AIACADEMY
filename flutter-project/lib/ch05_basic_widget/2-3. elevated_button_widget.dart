import 'package:flutterproject/ch05_basic_widget/2-2. outlined_button_widget.dart';
import 'package:flutter/material.dart';

class ElevatedButtonWidgetExample extends StatelessWidget {
  const ElevatedButtonWidgetExample({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: ElevatedButton(
            // 클릭 시 실행할 함수
            onPressed: (){},
            // 버튼 스타일링
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.red,
            ),
            // 버튼에 들어갈 위젯
            child: const Text('Elevated Button'),
          ),
        ),
      ),
    );
  }
}
