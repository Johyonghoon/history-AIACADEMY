import 'package:flutterproject/ch05_basic_widget/2-2. outlined_button_widget.dart';
import 'package:flutter/material.dart';

class IconButtonWidgetExample extends StatelessWidget {
  const IconButtonWidgetExample({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: IconButton(
            onPressed: () {},
            icon: const Icon(
              Icons.home,
            ),
          ),
        ),
      ),
    );
  }
}

