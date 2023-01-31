import 'package:flutter/material.dart';
import 'package:flutterproject/ch21_counter/provider/counter_provider.dart';
import 'package:flutterproject/ch21_counter/screen/counter_screen.dart';
import 'package:provider/provider.dart';

class HomeScreen extends StatelessWidget {
  HomeScreen({Key? key}) : super(key: key);
  late CounterProvider _counterProvider;

  @override
  Widget build(BuildContext context) {
    _counterProvider = Provider.of<CounterProvider>(context, listen: false);
    return Scaffold(
      appBar: AppBar(
        title: const Text("카운터", style: TextStyle(color: Colors.black, fontSize: 50.0)),
      ),
      body: const CounterScreen(),
      floatingActionButton: Row(
        mainAxisAlignment: MainAxisAlignment.end,
        children: [
          IconButton(onPressed: () => _counterProvider.increase(), icon: const Icon(Icons.add, size: 50,)),
          IconButton(onPressed: () => _counterProvider.decrease(), icon: const Icon(Icons.remove, size: 50,)),
        ],
      ),
    );
  }
}
