import 'package:auto_deploy_ma/core/components/mode_selector.dart';
import 'package:auto_deploy_ma/features/tic_tac_toe/components/tic_tac_toe_cell.dart';
import 'package:flutter/material.dart';

import './tic_tac_toe_view_model.dart';

class TicTacToeView extends TicTacToeViewModel {
  @override
  Widget build(BuildContext context) {
    final primary = Colors.blue;
    final secondary = Theme.of(context).colorScheme.secondary;
    final highlight = const Color(0xFF38BDF8);
    final bg = Theme.of(context).scaffoldBackgroundColor;

    Widget buildModeSelector() {
      return ModeSelector(
        title: 'Joguinho da velha',
        description: 'escolha o modo',
        options: [
          ModeSelectorOption(
            label: '1 jogador',
            icon: Icons.person,
            color: primary,
            onTap: () => selectMode(1),
          ),
          ModeSelectorOption(
            label: '2 jogadores',
            icon: Icons.people,
            color: highlight,
            onTap: () => selectMode(2),
          ),
        ],
      );
    }

    Widget buildBoard() {
      return Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
            winner != null
                ? 'ganhou papai'
                : isBoardFull
                ? 'escolha'
                : 'jogador atual',
            style: TextStyle(
              fontSize: 22,
              fontWeight: FontWeight.bold,
              color:
                  winner != null
                      ? highlight
                      : currentPlayer == 'X'
                      ? primary
                      : secondary,
              fontFamily: 'Montserrat',
            ),
          ),
          const SizedBox(height: 24),
          Container(
            decoration: BoxDecoration(
              color: Colors.white.withValues(alpha: 0.7),
              borderRadius: BorderRadius.circular(24),
              boxShadow: [
                BoxShadow(
                  color: primary.withValues(alpha: 0.08),
                  blurRadius: 16,
                  offset: const Offset(0, 8),
                ),
              ],
            ),
            padding: const EdgeInsets.all(16),
            child: GridView.builder(
              shrinkWrap: true,
              itemCount: 9,
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 3,
                crossAxisSpacing: 12,
                mainAxisSpacing: 12,
              ),
              itemBuilder: (context, i) {
                return TicTacToeCell(
                  value: board[i],
                  onTap: () => makeMove(i),
                  highlight: winner != null && board[i] == winner,
                  primary: primary,
                  secondary: secondary,
                );
              },
            ),
          ),
          const SizedBox(height: 24),
          ElevatedButton.icon(
            style: ElevatedButton.styleFrom(
              backgroundColor: highlight,
              foregroundColor: Colors.white,
              padding: const EdgeInsets.symmetric(horizontal: 32, vertical: 16),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(16),
              ),
              textStyle: const TextStyle(
                fontFamily: 'Montserrat',
                fontWeight: FontWeight.bold,
              ),
            ),
            onPressed: resetGame,
            icon: const Icon(Icons.refresh),
            label: Text('Restart'),
          ),
        ],
      );
    }

    return Scaffold(
      backgroundColor: bg,
      appBar: AppBar(
        title: Text('Joguinho da velha'),
        centerTitle: true,
        backgroundColor: primary,
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: gameMode == null ? buildModeSelector() : buildBoard(),
        ),
      ),
    );
  }
}
