import 'package:flutter/material.dart';
import 'package:flutterproject/ch23_caculator_37/components/button.dart';
import 'package:flutterproject/ch23_caculator_37/components/button_row.dart';

class Keyboard extends StatelessWidget {

  final void Function(String) onPressed;

  const Keyboard({super.key, required this.onPressed});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 500,
      child: Column(
        children: <Widget>[
          ButtonRow(
            buttons: [
              Button.large(
                text: 'AC',
                color: Button.darkButtonColor,
                onPressed: onPressed,
              ),
              Button(
                text: '%',
                color: Button.darkButtonColor,
                onPressed: onPressed,
              ),
              Button.operation(
                text: '/',
                onPressed: onPressed,
              ),
            ],
          ),
          const SizedBox(height: 1),
          ButtonRow(
            buttons: [
              Button(
                text: '7',
                onPressed: onPressed,
              ),
              Button(
                text: '8',
                onPressed: onPressed,
              ),
              Button(
                text: '9',
                onPressed: onPressed,
              ),
              Button.operation(
                text: 'x',
                onPressed: onPressed,
              ),
            ],
          ),
          const SizedBox(height: 1),
          ButtonRow(
            buttons: [
              Button(
                text: '4',
                onPressed: onPressed,
              ),
              Button(
                text: '5',
                onPressed: onPressed,
              ),
              Button(
                text: '6',
                onPressed: onPressed,
              ),
              Button.operation(
                text: '-',
                onPressed: onPressed,
              ),
            ],
          ),
          const SizedBox(height: 1),
          ButtonRow(
            buttons: [
              Button(
                text: '1',
                onPressed: onPressed,
              ),
              Button(
                text: '2',
                onPressed: onPressed,
              ),
              Button(
                text: '3',
                onPressed: onPressed,
              ),
              Button.operation(
                text: '+',
                onPressed: onPressed,
              ),
            ],
          ),
          const SizedBox(height: 1),
          ButtonRow(
            buttons: [
              Button.large(
                text: '0',
                onPressed: onPressed,
              ),
              Button(
                text: '.',
                onPressed: onPressed,
              ),
              Button.operation(
                text: '=',
                onPressed: onPressed,
              ),
            ],
          ),
        ],
      ),

    );
  }
}