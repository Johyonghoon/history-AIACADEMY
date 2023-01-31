import 'package:flutter/material.dart';
import 'package:flutterproject/ch22_calculator/main.dart';
import 'package:provider/provider.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("계산기", style: TextStyle(fontSize: 50),),),
      body: Center(),
      floatingActionButton: Row(
        children: [
          IconButton(onPressed: null, icon: Icon(Icons.add, size: 50,)),
          IconButton(onPressed: null, icon: Icon(Icons.remove, size: 50,)),
          IconButton(onPressed: null, icon: Icon(Icons.add, size: 50,)),
          IconButton(onPressed: null, icon: Icon(Icons.remove, size: 50,)),
        ],
      ),
    );
  }
}
