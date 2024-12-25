namespace Day02
{
    using System;
    using System.IO;

    class Program
    {
        public static void Main(string[] args)
        {
            Input input = new Input(args[0]);
            int solution1 = Solution.PartOne(input.Lines);
            Console.WriteLine($"The solution to part one: {solution1}");
            int solution2 = Solution.PartTwo(input.Lines);
            Console.WriteLine($"The solution to part two: {solution2}");
        }
    }

    class Solution
    {
        public static int PartOne(List<List<int>> lines)
        {
            int numSafe = 0;
            foreach (var line in lines)
            {
                Report report = new Report(line);
                if (report.CheckRates()) numSafe += 1;
            }
            return numSafe;
        }

        public static int PartTwo(List<List<int>> lines)
        {
            int numSafe = 0;
            foreach (var line in lines)
            {
                // Evaluate a copy of each report having each copy missing a different
                // item from the original report.
                // If at least one copy is safe, then the original report is safe
                for (int i = 0; i < line.Count; i++)
                {
                    List<int> copy = line.ToList();
                    copy.RemoveAt(i);
                    Report report = new Report(copy);
                    if (report.CheckRates())
                    {
                        numSafe += 1;
                        break;
                    }
                }
            }
            return numSafe;
        }
    }

    class Report(List<int> Levels)
    {
        public List<int> Levels { get; } = Levels;
        public List<int> Rates
        {
            get
            {
                List<int> rates = [];
                for (int i = 0; i < Levels.Count - 1; i++)
                {
                    int rate = Levels[i + 1] - Levels[i];
                    rates.Add(rate);
                }
                return rates;
            }
        }

        public bool CheckRates()
        {
            List<int> rates = Rates;

            int rangeChecks = 0;
            int directionCheck = 0;
            foreach (int rate in rates)
            {
                if (Math.Abs(rate) > 0 && Math.Abs(rate) <= 3) rangeChecks += 1;
                directionCheck += (rate > 0) ? 1 : (rate < 0) ? -1 : 0;
            }

            return (rangeChecks == rates.Count) && (Math.Abs(directionCheck) == rates.Count);
        }
    }

    class Input
    {
        public List<List<int>> Lines { get; }

        public Input(string filename)
        {
            Lines = [];
            if (File.Exists(filename))
            {
                using StreamReader sr = new StreamReader(filename);
                string? line = string.Empty;
                while ((line = sr.ReadLine()) != null)
                {
                    string[] parts = line.Split(" ");
                    var Line = parts.ToList().ConvertAll(int.Parse);
                    Lines.Add(Line);
                }
            }

        }
    }

}