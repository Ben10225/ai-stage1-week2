# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from task2 import Point, Enemy, Tower, Game
import math


class TestPoint(unittest.TestCase):
    def test_distance(self):
        p1 = Point(x=0, y=0)
        p2 = Point(x=3, y=4)
        self.assertEqual(p1.distance_to(p2), 5.0)

        p3 = Point(x=-1, y=-1)
        self.assertEqual(p1.distance_to(p3), math.sqrt(2))


class TestEnemy(unittest.TestCase):
    def test_move_and_take_damage(self):
        start_pos = Point(x=0, y=0)
        enemy = Enemy(label="EE", start_pos=start_pos, velocity=(1, 1))

        # 初始位置
        self.assertEqual((enemy.pos.x, enemy.pos.y), (0, 0))

        # 移動一次
        enemy.move()
        self.assertEqual((enemy.pos.x, enemy.pos.y), (1, 1))

        # 受到傷害
        enemy.take_damage(3)
        self.assertEqual(enemy.hp, 7)

        # 移動直到被消滅
        for _ in range(7):
            enemy.take_damage(1)
        self.assertEqual(enemy.hp, 0)

        # 嘗試移動，位置應該不變
        enemy.move()
        self.assertEqual((enemy.pos.x, enemy.pos.y), (1, 1))


class TestTower(unittest.TestCase):
    def test_can_attack(self):
        tower_basic = Tower(label="Basic", position=Point(x=0, y=0))
        tower_advanced = Tower(label="Advanced", position=Point(x=0, y=0))

        enemy_pos_within_basic = Point(x=1, y=1)
        enemy_pos_outside_basic = Point(x=2, y=2)

        self.assertTrue(tower_basic.can_attack(enemy_pos_within_basic))
        self.assertFalse(tower_basic.can_attack(enemy_pos_outside_basic))

        enemy_pos_within_advanced = Point(x=2, y=2)
        enemy_pos_outside_advanced = Point(x=3, y=3)

        self.assertTrue(tower_advanced.can_attack(enemy_pos_within_advanced))
        self.assertFalse(tower_advanced.can_attack(enemy_pos_outside_advanced))


class TestGame(unittest.TestCase):
    def test_one_turn_todo(self):
        enemy1 = Enemy(label="E1", start_pos=Point(x=0, y=0), velocity=(1, 0))
        enemy2 = Enemy(label="E2", start_pos=Point(x=5, y=5), velocity=(0, -1))

        tower1 = Tower(label="Basic", position=Point(x=2, y=0))
        tower2 = Tower(label="Advanced", position=Point(x=5, y=3))

        game = Game(enemies=[enemy1, enemy2], towers=[tower1, tower2])

        # 執行一回合
        game.execute_turn()

        # 檢查敵人位置和血量
        self.assertEqual((enemy1.pos.x, enemy1.pos.y), (1, 0))
        self.assertEqual(enemy1.hp, 9)  # 被 tower Basic 攻擊

        self.assertEqual((enemy2.pos.x, enemy2.pos.y), (5, 4))
        self.assertEqual(enemy2.hp, 8)  # 被 tower Advanced 攻擊

    def test_run(self):
        enemy = Enemy(label="E1", start_pos=Point(x=0, y=0), velocity=(1, 0))
        tower = Tower(label="Basic", position=Point(x=2, y=0))

        game = Game(enemies=[enemy], towers=[tower])

        # 執行 3 回合
        game.run(turns=3)

        # 檢查敵人位置和血量
        self.assertEqual((enemy.pos.x, enemy.pos.y), (3, 0))
        self.assertEqual(enemy.hp, 7)  # 被 tower Basic 攻擊了 3 次


if __name__ == "__main__":
    unittest.main()
