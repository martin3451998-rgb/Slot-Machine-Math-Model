import random


class SlotMachine:
    def __init__(self):
        self.reel1 = ['7'] * 1 + ['B'] * 3 + ['P'] * 10 + ['C'] * 18
        self.reel2 = ['7'] * 2 + ['B'] * 4 + ['P'] * 10 + ['C'] * 16
        self.reel3 = ['7'] * 1 + ['B'] * 5 + ['P'] * 10 + ['C'] * 16

        self.paytable = {
            '7': 150,
            'B': 40,
            'P': 10,
            'C': 4
        }

    def spin(self):
        stop1 = random.choice(self.reel1)
        stop2 = random.choice(self.reel2)
        stop3 = random.choice(self.reel3)

        if stop1 == stop2 == stop3:
            symbol = stop1
            return self.paytable[symbol]
        else:
            return 0


def run_simulation(spins):
    machine = SlotMachine()
    total_bet = spins * 1
    total_win = 0
    total_hits = 0

    print(f"Starting simulation of {spins:,} spins...")

    for _ in range(spins):
        win = machine.spin()
        if win > 0:
            total_win += win
            total_hits += 1

    rtp = (total_win / total_bet) * 100
    hit_frequency = (total_hits / spins) * 100

    print("\n--- SIMULATION RESULTS ---")
    print(f"Total Bet: {total_bet:,} credits")
    print(f"Total Win: {total_win:,} credits")
    print(f"Simulated RTP: {rtp:.2f}% (Theoretical: 95.007%)")
    print(f"Simulated Hit Frequency: {hit_frequency:.2f}% (Theoretical: 17.303%)")


if __name__ == "__main__":
    run_simulation(1000000)
