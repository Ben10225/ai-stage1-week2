from __future__ import annotations
from typing import Tuple, Literal
import math


class Point:
    def __init__(self, *, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def distance_to(self, other: Point) -> float:
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


class Enemy:
    def __init__(
        self, *, label: str, start_pos: Point, velocity: Tuple[int, int]
    ) -> None:
        self.label = label
        self.pos = start_pos
        self.velocity = velocity
        self.hp = 10

    def move(
        self,
    ):
        if self.hp <= 0:
            return self.pos  # 已被消滅，位置不變

        self.pos.x += self.velocity[0]
        self.pos.y += self.velocity[1]

    def take_damage(self, damage: int) -> None:
        if self.hp > 0:
            self.hp -= damage


class Tower:
    def __init__(self, *, label: Literal["Basic", "Advanced"], position: Point) -> None:
        self.position = position
        self.attack_points = 1 if label == "Basic" else 2
        self.range = 2 if label == "Basic" else 4

    def can_attack(self, enemy_pos: Point) -> bool:
        distance = self.position.distance_to(enemy_pos)
        return distance <= self.range


class Game:

    def __init__(self, *, enemies: list[Enemy], towers: list[Tower]) -> None:
        self.enemies = enemies
        self.towers = towers

    def execute_turn(self) -> None:
        for enemy in self.enemies:
            enemy.move()

            for tower in self.towers:
                if tower.can_attack(enemy.pos):
                    enemy.take_damage(tower.attack_points)
                    # print(
                    #     f"Turn { now_turn }: Tower at ({tower.position.x}, {tower.position.y}) attacks Enemy {enemy.label} at ({enemy.pos.x}, {enemy.pos.y}) for {tower.attack_points} damage. Enemy HP is now {enemy.hp}."
                    # )

    def run(self, *, turns: int) -> None:
        # 跑十次
        for _ in range(1, turns + 1):
            self.execute_turn()

        # 結束遊戲
        for enemy in self.enemies:
            print(
                f"Enemy {enemy.label}: final position is ({enemy.pos.x}, {enemy.pos.y}) and life points is {enemy.hp}."
            )


def main() -> None:
    enemy1_start_pos = Point(x=-10, y=2)
    enemy2_start_pos = Point(x=-8, y=0)
    enemy3_start_pos = Point(x=-9, y=-1)

    enemy1 = Enemy(label="E1", start_pos=enemy1_start_pos, velocity=(2, -1))
    enemy2 = Enemy(label="E2", start_pos=enemy2_start_pos, velocity=(3, 1))
    enemy3 = Enemy(label="E3", start_pos=enemy3_start_pos, velocity=(3, 0))

    enemies = [enemy1, enemy2, enemy3]

    tower_t1_pos = Point(x=-3, y=2)
    tower_t2_pos = Point(x=-1, y=-2)
    tower_t3_pos = Point(x=4, y=2)
    tower_t4_pos = Point(x=7, y=0)
    tower_a1_pos = Point(x=1, y=1)
    tower_a2_pos = Point(x=4, y=-3)

    tower1 = Tower(label="Basic", position=tower_t1_pos)
    tower2 = Tower(label="Basic", position=tower_t2_pos)
    tower3 = Tower(label="Basic", position=tower_t3_pos)
    tower4 = Tower(label="Basic", position=tower_t4_pos)
    tower5 = Tower(label="Advanced", position=tower_a1_pos)
    tower6 = Tower(label="Advanced", position=tower_a2_pos)

    towers = [tower1, tower2, tower3, tower4, tower5, tower6]

    game = Game(enemies=enemies, towers=towers)
    game.run(turns=10)


if __name__ == "__main__":
    main()
