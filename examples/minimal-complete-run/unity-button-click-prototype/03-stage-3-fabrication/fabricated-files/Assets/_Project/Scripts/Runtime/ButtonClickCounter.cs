namespace ButtonClickPrototype.Runtime
{
    /// <summary>
    /// Pure counter model for the Button Click Prototype.
    /// </summary>
    public sealed class ButtonClickCounter
    {
        public int Count { get; private set; }

        public int Increment()
        {
            Count += 1;
            return Count;
        }

        public void Reset()
        {
            Count = 0;
        }
    }
}
