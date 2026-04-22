import math
import random

import pylab

# =====================================================
# Даалгавар 1: Зоос шидэх симуляц
# =====================================================


def sim_coin_flips(num_flips):
    """num_flips удаа зоос шидэж, 'Heads' буух хувийг буцаана."""
    heads_count = 0
    for i in range(num_flips):
        coin = random.choice(["H", "T"])
        if coin == "H":
            heads_count += 1
    return heads_count / num_flips


for n in [10, 100, 1000, 10000, 1000000]:
    print(f"{sim_coin_flips(n):.4f}")


# =====================================================
# Даалгавар 2: Санамсаргүй алхалт
# =====================================================


class SimpleLocation:
    """2 хэмжээст байршлыг илэрхийлэх класс."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        """Шинэ байршлын SimpleLocation объект буцаана."""
        return SimpleLocation(self.x + dx, self.y + dy)

    def get_dist(self, other):
        """Евклидийн зайг буцаана."""
        return math.sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))


def one_dimension_walk(num_steps):
    """1 хэмжээст санамсаргүй алхалт явуулж эцсийн байршлыг буцаана."""
    # TODO: random.choice([1, -1]), current.x буцаа
    location = SimpleLocation(0, 0)
    current = location
    for i in range(num_steps):
        movement = random.choice([1, -1])
        current = current.move(movement, 0)
    return current


# =====================================================
# Даалгавар 3: Статистик дүн шинжилгээ
# =====================================================

NUM_TRIALS = 50
NUM_STEPS = 100
origin = SimpleLocation(0, 0)

end_positions = []
distances = []

for _ in range(NUM_TRIALS):
    final_loc = one_dimension_walk(NUM_STEPS)
    end_positions.append(final_loc.x)
    dist = final_loc.get_dist(origin)
    distances.append(dist)

avg_dist = sum(distances) / len(distances)
max_dist = max(distances)
min_dist = min(distances)

print("\n--- Даалгавар 3 ---")
print(f"Дундаж зай: {avg_dist:.2f}")
print(f"Хамгийн их зай: {max_dist:.2f}")
print(f"Хамгийн бага зай: {min_dist:.2f}")

# TODO: дундаж, хамгийн их, хамгийн бага зайг хэвлэх


# =====================================================
# Даалгавар 4: Графикаар дүрслэх
# =====================================================

# TODO: pylab.scatter, pylab.axhline(0)
pylab.figure(figsize=(10, 6))
pylab.scatter(
    range(1, NUM_TRIALS + 1), end_positions, color="blue", label="Эцсийн байршил"
)
pylab.axhline(0, color="red", linestyle="--", label="Эхлэл (y=0)")

pylab.title(f"Санамсаргүй алхалтын үр дүн ({NUM_TRIALS} туршилт)")
pylab.xlabel("Туршилтын дугаар")
pylab.ylabel("Эцсийн байршил (x)")
pylab.grid(True, linestyle=":", alpha=0.6)
pylab.legend()
# pylab.show()
pylab.savefig("random_walk_result.png")
