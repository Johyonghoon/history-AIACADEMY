import 'package:flutter/cupertino.dart';

class CountProvider extends ChangeNotifier{
  int _count = 0;
  int get count => _count;

  void increase() {
    ++_count;
    notifyListeners();
  }
  void decrease() {
    --_count;
    notifyListeners();
  }
}
