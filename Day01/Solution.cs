using System;
using System.IO;


namespace AdventOfCode2024
{
    namespace Day01
    {
        class Solution
        {
            public static void Main(String[] args)
            {
                InputFile input = new InputFile("/home/churd/projects/adventofcode2024/Day01/input.txt");
                int solution1 = PartOne(input.Locations[0], input.Locations[1]);
                Console.WriteLine($"The solution to part one: {solution1}");
                int solution2 = PartTwo(input.Locations[0], input.Locations[1]);
                Console.WriteLine($"The solution to part two: {solution2}");
            }

            public static int PartOne(List<int> a, List<int> b)
            {
                a.Sort();
                b.Sort();
                int dist = 0;
                for (var i = 0; i < a.Count; i++)
                {
                    dist += Math.Abs(a[i] - b[i]);
                }

                return dist;
            }

            static int PartTwo(List<int> a, List<int> b)
            {
                int score = 0;
                for (int i = 0; i < a.Count; i++)
                {
                    int val = a[i];
                    int freq = b.FindAll(x => x == val).Count();
                    score += val * freq;
                }
                return score;
            }

        }
    }

    class InputFile
    {
        public List<List<int>> Locations { get; }

        public InputFile(string filename)
        {
            this.Locations = new List<List<int>> { new List<int>(), new List<int>() };
            if (File.Exists(filename))
            {
                using (StreamReader sr = new StreamReader(filename))
                {
                    string? line = string.Empty;
                    while ((line = sr.ReadLine()) != null)
                    {
                        string[] parts = line.Split("   ");
                        this.Locations[0].Add(Int32.Parse(parts[0]));
                        this.Locations[1].Add(Int32.Parse(parts[1]));
                    }
                }
            }

        }

    }
}
