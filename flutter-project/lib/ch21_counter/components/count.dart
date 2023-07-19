import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutterproject/ch21_counter/provider/count_provider.dart';
import 'package:provider/provider.dart';

class Count extends StatelessWidget {

  const Count({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Consumer<CountProvider>(
          builder: (context, counterProvider, child) => Text(
            Provider.of<CountProvider>(context).count.toString(),
            style: TextStyle(fontSize: 60),
          )
      ),
    );
  }
}