class GenerateData:
    @staticmethod
    def clear_files():
        with open("data/rects.txt", mode="w") as f:
            pass
        with open("data/points.txt", mode="w") as f:
            pass

    @staticmethod
    def generate_points(n):
        with open("data/rects.txt", mode="a") as f1:
            with open("data/rects_session.txt", mode="w") as f2:
                for i in range(n):
                    f1.write(f"{10*i} {10*i} {10*(2*n-i)} {10*(2*n-i)}\n")
                    f2.write(f"{10*i} {10*i} {10*(2*n-i)} {10*(2*n-i)}\n")
                f1.write("=" * 100 + "\n")

    @staticmethod
    def generate_rects(n):
        with open("data/points.txt", mode="a") as f1:
            with open("data/points_session.txt", mode="w") as f2:
                for i in range(n):
                    f1.write(f"{(1423*i)**31%(20*n)} {(1583*i)**31%(20*n)}\n")
                    f2.write(f"{(1423*i)**31%(20*n)} {(1583*i)**31%(20*n)}\n")
                f1.write("=" * 100 + '\n')