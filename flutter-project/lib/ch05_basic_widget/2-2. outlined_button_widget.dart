import 'package:flutter/material.dart';

class OutlinedButtonWidgetExample extends StatelessWidget {
  const OutlinedButtonWidgetExample({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: OutlinedButton(
            // 클릭 시 실행할 함수
            onPressed: () {},
            // 버튼 스타일
            style: OutlinedButton.styleFrom(
              foregroundColor: Colors.red,
            ),
            // 버튼에 들어갈 위젯
            child: const Text('Outlined Button'),
          ),
        ),
      ),
    );
  }
}