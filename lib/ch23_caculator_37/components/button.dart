import 'package:flutter/material.dart';

class Button extends StatelessWidget {
  final String text;
  final bool isBig;
  final Color color;
  final void Function(String) onPressed;
  static const defaultButtonColor = Color.fromRGBO(112, 112, 112, 1);
  static const darkButtonColor = Color.fromRGBO(82, 82, 82, 1);
  static const operationButtonColor = Color.fromRGBO(250, 158, 13, 1);

  const Button({
    required this.text,
    this.isBig = true,
    this.color = Button.defaultButtonColor,
    required this.onPressed,
    super.key});

  const Button.operation({
    required this.text,
    this.isBig = true,
    this.color = Button.operationButtonColor,
    required this.onPressed,
    super.key});

  const Button.large({
    required this.text,
    this.isBig = true,
    this.color = Button.darkButtonColor,
    required this.onPressed,
    super.key});


  @override
  Widget build(BuildContext context) {
    return Expanded(
        flex: isBig ? 2 : 1,
        child: ElevatedButton(
          style: ElevatedButton.styleFrom(backgroundColor: color),
          onPressed: () => onPressed(text),
          child: Text(
              style: const TextStyle(
                  color: Colors.white,
                  fontSize: 32,
                  fontWeight: FontWeight.w200),
              text),
        ));
  }
}
