using ButtonClickPrototype.Runtime;
using NUnit.Framework;

namespace ButtonClickPrototype.Tests.EditMode
{
    public sealed class ButtonClickCounterTests
    {
        [Test]
        public void Increment_IncreasesCountByOne()
        {
            var counter = new ButtonClickCounter();

            var result = counter.Increment();

            Assert.That(result, Is.EqualTo(1));
            Assert.That(counter.Count, Is.EqualTo(1));
        }

        [Test]
        public void Reset_ReturnsCountToZero()
        {
            var counter = new ButtonClickCounter();
            counter.Increment();

            counter.Reset();

            Assert.That(counter.Count, Is.EqualTo(0));
        }
    }
}
