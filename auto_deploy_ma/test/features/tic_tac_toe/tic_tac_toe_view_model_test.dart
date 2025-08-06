import 'package:auto_deploy_ma/core/core.dart';
import 'package:auto_deploy_ma/features/tic_tac_toe/tic_tac_toe_view_model.dart';

import 'package:flutter_test/flutter_test.dart';

void main() {
  group('home view model test', () {
    TestWidgetsFlutterBinding.ensureInitialized();

    setUpAll(() {});

    test('selectMode', () async {
      const feature = TicTacToe();
      final view = feature.createElement();
      final viewModel = view.state as TicTacToeViewModel;

      int gameMode = 0;
      viewModel.selectMode(gameMode);

      expect(viewModel.gameMode, gameMode);
      expect(viewModel.winner, null);
      expect(viewModel.currentPlayer, 'X');
    });

    test('resetGame', () async {
      const feature = TicTacToe();
      final view = feature.createElement();
      final viewModel = view.state as TicTacToeViewModel;

      viewModel.resetGame();

      expect(viewModel.gameMode, null);
      expect(viewModel.winner, null);
      expect(viewModel.currentPlayer, 'X');
    });

    test('makeMove', () async {
      const feature = TicTacToe();
      final view = feature.createElement();
      final viewModel = view.state as TicTacToeViewModel;

      int index = 0;
      viewModel.makeMove(index);

      expect(viewModel.board[index], 'X');
    });

    test('checkWinner null', () async {
      const feature = TicTacToe();
      final view = feature.createElement();
      final viewModel = view.state as TicTacToeViewModel;

      viewModel.checkWinner();

      expect(viewModel.winner, null);
    });

    test('checkWinner with winner', () async {
      const feature = TicTacToe();
      final view = feature.createElement();
      final viewModel = view.state as TicTacToeViewModel;

      viewModel.selectMode(2);
      viewModel.makeMove(0); // X at position 0
      viewModel.makeMove(3); // O at position 3
      viewModel.makeMove(1); // X at position 1
      viewModel.makeMove(4); // O at position 4
      viewModel.makeMove(2); // X at position 2 (wins)

      expect(viewModel.winner, 'X');
    });
  });
}
