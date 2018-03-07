---
title: Markdown記法
date: 2018-03-04 15:35:39
tags: Markdown
---

# [Markdown記法 サンプル集 - Qiita](https://qiita.com/tbpgr/items/989c6badefff69377da7)


<section class="it-MdContent" itemprop="articleBody"><div id="item-989c6badefff69377da7">
<h1>
<span id="-markdown記法-サンプル集" class="fragment"></span><a href="#-markdown%E8%A8%98%E6%B3%95-%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB%E9%9B%86"><i class="fa fa-link"></i></a><i></i> Markdown記法 サンプル集</h1>

<h2>
<span id="-見出し" class="fragment"></span><a href="#-%E8%A6%8B%E5%87%BA%E3%81%97"><i class="fa fa-link"></i></a><i></i> 見出し</h2>

<p>1個から6個シャープで見出しを記述する。</p>

<h3>
<span id="-記述例" class="fragment"></span><a href="#-%E8%A8%98%E8%BF%B0%E4%BE%8B"><i class="fa fa-link"></i></a><i></i> 記述例</h3>

<div class="code-frame" data-lang="md"><div class="highlight"><pre><span class="gh"># 見出し1</span>
<span class="gu">## 見出し2</span>
<span class="gu">### 見出し3</span>
<span class="gu">#### 見出し4</span>
<span class="gu">##### 見出し5</span>
<span class="gu">###### 見出し6</span>
</pre></div></div>

<h3>
<span id="表示例" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B"><i class="fa fa-link"></i></a>表示例</h3>

<h1>
<span id="見出し1" class="fragment"></span><a href="#%E8%A6%8B%E5%87%BA%E3%81%971"><i class="fa fa-link"></i></a>見出し1</h1>

<h2>
<span id="見出し2" class="fragment"></span><a href="#%E8%A6%8B%E5%87%BA%E3%81%972"><i class="fa fa-link"></i></a>見出し2</h2>

<h3>
<span id="見出し3" class="fragment"></span><a href="#%E8%A6%8B%E5%87%BA%E3%81%973"><i class="fa fa-link"></i></a>見出し3</h3>

<h4>
<span id="見出し4" class="fragment"></span><a href="#%E8%A6%8B%E5%87%BA%E3%81%974"><i class="fa fa-link"></i></a>見出し4</h4>

<h5>
<span id="見出し5" class="fragment"></span><a href="#%E8%A6%8B%E5%87%BA%E3%81%975"><i class="fa fa-link"></i></a>見出し5</h5>

<h6>
<span id="見出し6" class="fragment"></span><a href="#%E8%A6%8B%E5%87%BA%E3%81%976"><i class="fa fa-link"></i></a>見出し6</h6>

<h2>
<span id="-箇条書きリスト" class="fragment"></span><a href="#-%E7%AE%87%E6%9D%A1%E6%9B%B8%E3%81%8D%E3%83%AA%E3%82%B9%E3%83%88"><i class="fa fa-link"></i></a><i></i> 箇条書きリスト</h2>

<p>ハイフン、プラス、アスタリスクのいずれかで箇条書きリストを記述可能。</p>

<h3>
<span id="記述例" class="fragment"></span><a href="#%E8%A8%98%E8%BF%B0%E4%BE%8B"><i class="fa fa-link"></i></a>記述例</h3>

<div class="code-frame" data-lang="md"><div class="highlight"><pre><span class="p">-</span> リスト1
<span class="p">    -</span> ネスト リスト1_1
<span class="p">        -</span> ネスト リスト1_1_1
<span class="p">        -</span> ネスト リスト1_1_2
<span class="p">    -</span> ネスト リスト1_2
<span class="p">-</span> リスト2
<span class="p">-</span> リスト3
</pre></div></div>

<h3>
<span id="表示例-1" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B-1"><i class="fa fa-link"></i></a>表示例</h3>

<ul>
<li>リスト1

<ul>
<li>ネスト リスト1_1

<ul>
<li>ネスト リスト1_1_1</li>
<li>ネスト リスト1_1_2</li>
</ul>
</li>
<li>ネスト リスト1_2</li>
</ul>
</li>
<li>リスト2</li>
<li>リスト3</li>
</ul>

<h2>
<span id="-番号付きリスト" class="fragment"></span><a href="#-%E7%95%AA%E5%8F%B7%E4%BB%98%E3%81%8D%E3%83%AA%E3%82%B9%E3%83%88"><i class="fa fa-link"></i></a><i></i> 番号付きリスト</h2>

<h3>
<span id="記述例-1" class="fragment"></span><a href="#%E8%A8%98%E8%BF%B0%E4%BE%8B-1"><i class="fa fa-link"></i></a>記述例</h3>

<div class="code-frame" data-lang="md"><div class="highlight"><pre><span class="p">1.</span> 番号付きリスト1
<span class="p">    1.</span> 番号付きリスト1_1
<span class="p">    1.</span> 番号付きリスト1_2
<span class="p">1.</span> 番号付きリスト2
<span class="p">1.</span> 番号付きリスト3
</pre></div></div>

<h3>
<span id="表示例-2" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B-2"><i class="fa fa-link"></i></a>表示例</h3>

<ol>
<li>番号付きリスト1

<ol>
<li>番号付きリスト1_1</li>
<li>番号付きリスト1_2</li>
</ol>
</li>
<li>番号付きリスト2</li>
<li>番号付きリスト3</li>
</ol>

<h2>
<span id="-引用" class="fragment"></span><a href="#-%E5%BC%95%E7%94%A8"><i class="fa fa-link"></i></a><i></i> 引用</h2>

<div class="code-frame" data-lang="md"><div class="highlight"><pre><span class="gt">&gt; お世話になります。xxxです。</span>
<span class="gt">&gt; </span>
<span class="gt">&gt; ご連絡いただいた、バグの件ですが、仕様です。</span>
</pre></div></div>

<h3>
<span id="表示例-3" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B-3"><i class="fa fa-link"></i></a>表示例</h3>

<blockquote>
<p>お世話になります。xxxです。</p>

<p>ご連絡いただいた、バグの件ですが、仕様です。</p>
</blockquote>

<h2>
<span id="-二重引用" class="fragment"></span><a href="#-%E4%BA%8C%E9%87%8D%E5%BC%95%E7%94%A8"><i class="fa fa-link"></i></a><i></i> 二重引用</h2>

<h3>
<span id="記述例-2" class="fragment"></span><a href="#%E8%A8%98%E8%BF%B0%E4%BE%8B-2"><i class="fa fa-link"></i></a>記述例</h3>

<div class="code-frame" data-lang="md"><div class="highlight"><pre><span class="gt">&gt; お世話になります。xxxです。</span>
<span class="gt">&gt; </span>
<span class="gt">&gt; ご連絡いただいた、バグの件ですが、仕様です。</span>
<span class="gt">&gt;&gt; お世話になります。 yyyです。</span>
<span class="gt">&gt;&gt; </span>
<span class="gt">&gt;&gt; あの新機能バグってるっすね</span>
</pre></div></div>

<h3>
<span id="表示例-4" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B-4"><i class="fa fa-link"></i></a>表示例</h3>

<blockquote>
<p>お世話になります。xxxです。</p>

<p>ご連絡いただいた、バグの件ですが、仕様です。</p>

<blockquote>
<p>お世話になります。 yyyです。</p>

<p>あの新機能バグってるっすね</p>
</blockquote>
</blockquote>

<h2>
<span id="-pre記法スペース4-or-タブ" class="fragment"></span><a href="#-pre%E8%A8%98%E6%B3%95%E3%82%B9%E3%83%9A%E3%83%BC%E3%82%B94-or-%E3%82%BF%E3%83%96"><i class="fa fa-link"></i></a><i></i> pre記法(スペース4 or タブ)</h2>

<p>半角スペース4個もしくはタブで、コードブロックをpre表示できます</p>

<h3>
<span id="記述例-3" class="fragment"></span><a href="#%E8%A8%98%E8%BF%B0%E4%BE%8B-3"><i class="fa fa-link"></i></a>記述例</h3>

<div class="code-frame" data-lang="md"><div class="highlight"><pre>    # Tab
    class Hoge
        def hoge
            print 'hoge'
        end
    end
<span class="p">
---
</span>
    # Space
    class Hoge
      def hoge
        print 'hoge'
      end
    end
</pre></div></div>

<h3>
<span id="表示例-5" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B-5"><i class="fa fa-link"></i></a>表示例</h3>

<div class="code-frame" data-lang="text"><div class="highlight"><pre>class Hoge
    def hoge
        print 'hoge'
    end
end
</pre></div></div>

<hr>

<div class="code-frame" data-lang="text"><div class="highlight"><pre>class Hoge
  def hoge
    print 'hoge'
  end
end
</pre></div></div>

<h2>
<span id="-code記法" class="fragment"></span><a href="#-code%E8%A8%98%E6%B3%95"><i class="fa fa-link"></i></a><i></i> code記法</h2>

<p>バッククォートで文字列を囲むことでコードの一部を表示可能です。</p>

<h3>
<span id="記述例-4" class="fragment"></span><a href="#%E8%A8%98%E8%BF%B0%E4%BE%8B-4"><i class="fa fa-link"></i></a>記述例</h3>

<div class="code-frame" data-lang="md"><div class="highlight"><pre>インストールコマンドは <span class="sb">`gem install hoge`</span> です
</pre></div></div>

<h3>
<span id="表示例-6" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B-6"><i class="fa fa-link"></i></a>表示例</h3>

<p>インストールコマンドは <code>gem install hoge</code> です</p>

<h2>
<span id="-強調em" class="fragment"></span><a href="#-%E5%BC%B7%E8%AA%BFem"><i class="fa fa-link"></i></a><i></i> 強調：&lt;em&gt;</h2>

<p>アスタリスクもしくはアンダースコア1個で文字列を囲むことで強調します。<br>
見た目は斜体になります。</p>

<h3>
<span id="記述例-5" class="fragment"></span><a href="#%E8%A8%98%E8%BF%B0%E4%BE%8B-5"><i class="fa fa-link"></i></a>記述例</h3>

<div class="code-frame" data-lang="md"><div class="highlight"><pre>normal <span class="ge">*italic*</span> normal
normal _italic_ normal
</pre></div></div>

<h3>
<span id="表示例-7" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B-7"><i class="fa fa-link"></i></a>表示例</h3>

<p>normal <em>italic</em> normal<br>
normal <em>italic</em> normal</p>

<h2>
<span id="-強調strong" class="fragment"></span><a href="#-%E5%BC%B7%E8%AA%BFstrong"><i class="fa fa-link"></i></a><i></i> 強調：&lt;strong&gt;</h2>

<p>アスタリスクもしくはアンダースコア2個で文字列を囲むことで強調にします。<br>
見た目は太字になります。</p>

<h3>
<span id="記述例-6" class="fragment"></span><a href="#%E8%A8%98%E8%BF%B0%E4%BE%8B-6"><i class="fa fa-link"></i></a>記述例</h3>

<div class="code-frame" data-lang="md"><div class="highlight"><pre>normal <span class="gs">**bold**</span> normal
normal __bold__ normal
</pre></div></div>

<h3>
<span id="表示例-8" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B-8"><i class="fa fa-link"></i></a>表示例</h3>

<p>normal <strong>bold</strong> normal<br>
normal <strong>bold</strong> normal</p>

<h2>
<span id="-強調em--strong" class="fragment"></span><a href="#-%E5%BC%B7%E8%AA%BFem--strong"><i class="fa fa-link"></i></a><i></i> 強調：&lt;em&gt; + &lt;strong&gt;</h2>

<p>アスタリスクもしくはアンダースコア3個で文字列を囲むことで &lt;em&gt; と &lt;strong&gt; による強調を両方適用します。<br>
見た目は斜体かつ太字になります。</p>

<h3>
<span id="記述例-7" class="fragment"></span><a href="#%E8%A8%98%E8%BF%B0%E4%BE%8B-7"><i class="fa fa-link"></i></a>記述例</h3>

<div class="code-frame" data-lang="md"><div class="highlight"><pre>normal <span class="gs">***bold**</span><span class="err">*</span> normal
normal ___bold___ normal
</pre></div></div>

<h3>
<span id="表示例-9" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B-9"><i class="fa fa-link"></i></a>表示例</h3>

<p>normal <strong><em>bold</em></strong> normal<br>
normal <strong><em>bold</em></strong> normal</p>

<h2>
<span id="-水平線" class="fragment"></span><a href="#-%E6%B0%B4%E5%B9%B3%E7%B7%9A"><i class="fa fa-link"></i></a><i></i> 水平線</h2>

<p>アンダースコア、アスタリスク、ハイフンなどを3つ以上連続して記述することで水平線を表示します。<br>
※連続するハイフンなどの間にはスペースがあっても良い</p>

<h3>
<span id="記述例-8" class="fragment"></span><a href="#%E8%A8%98%E8%BF%B0%E4%BE%8B-8"><i class="fa fa-link"></i></a>記述例</h3>

<div class="code-frame" data-lang="markdown"><div class="highlight"><pre><span class="p">
***
</span>
<span class="ge">__</span>_
<span class="p">
---

*    *    *

</span></pre></div></div>

<h3>
<span id="表示例-10" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B-10"><i class="fa fa-link"></i></a>表示例</h3>

<hr>

<hr>

<hr>

<hr>

<h2>
<span id="-リンク" class="fragment"></span><a href="#-%E3%83%AA%E3%83%B3%E3%82%AF"><i class="fa fa-link"></i></a><i></i> リンク</h2>

<p><code>[表示文字](リンクURL)</code>形式でリンクを記述できます</p>

<div class="code-frame" data-lang="md"><div class="highlight"><pre><span class="p">[</span><span class="nv">Google先生</span><span class="p">](</span><span class="sx">https://www.google.co.jp/</span><span class="p">)</span>
</pre></div></div>

<p><a href="https://www.google.co.jp/" rel="nofollow noopener" target="_blank">Google先生</a></p>

<h2>
<span id="-定義参照リンク" class="fragment"></span><a href="#-%E5%AE%9A%E7%BE%A9%E5%8F%82%E7%85%A7%E3%83%AA%E3%83%B3%E3%82%AF"><i class="fa fa-link"></i></a><i></i> 定義参照リンク</h2>

<p>Markdownの文書の途中に長いリンクを記述したくない場合は、<br>
同じリンクの参照を何度も利用する場合は、リンク先への参照を定義することができます。</p>

<div class="code-frame" data-lang="markdown"><div class="highlight"><pre><span class="p">[</span><span class="nv">こっちからgoogle</span><span class="p">][</span><span class="ss">google</span><span class="p">]</span>
その他の文章
<span class="p">[</span><span class="nv">こっちからもgoogle</span><span class="p">][</span><span class="ss">google</span><span class="p">]</span><span class="sb">


</span></pre></div></div>

<p><a href="https://www.google.co.jp/" rel="nofollow noopener" target="_blank">こっちからgoogle</a><br>
その他の文章<br>
<a href="https://www.google.co.jp/" rel="nofollow noopener" target="_blank">こっちからもgoogle</a></p>

<h2>
<span id="-github-flavored-markdowngfm" class="fragment"></span><a href="#-github-flavored-markdowngfm"><i class="fa fa-link"></i></a><i></i> GitHub Flavored Markdown(GFM)</h2>

<p>GitHub Flavored Markdown(GFM)はGitHubの独自仕様を加えたMarkdown記法。<br>
以降、GFMと記載します。</p>

<h2>
<span id="-gfmリンクテキスト簡易記法" class="fragment"></span><a href="#-gfm%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E7%B0%A1%E6%98%93%E8%A8%98%E6%B3%95"><i class="fa fa-link"></i></a><i></i> GFM:リンクテキスト簡易記法</h2>

<p>URLは記述するだけで自動的にリンクになります。</p>

<h3>
<span id="記述例-9" class="fragment"></span><a href="#%E8%A8%98%E8%BF%B0%E4%BE%8B-9"><i class="fa fa-link"></i></a>記述例</h3>

<div class="code-frame" data-lang="md"><div class="highlight"><pre>https://www.google.co.jp/
</pre></div></div>

<h3>
<span id="表示例-11" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B-11"><i class="fa fa-link"></i></a>表示例</h3>

<p><a href="https://www.google.co.jp/" class="autolink" rel="nofollow noopener" target="_blank">https://www.google.co.jp/</a></p>

<h2>
<span id="-gfm取り消し線" class="fragment"></span><a href="#-gfm%E5%8F%96%E3%82%8A%E6%B6%88%E3%81%97%E7%B7%9A"><i class="fa fa-link"></i></a><i></i> GFM:取り消し線</h2>

<p>チルダ2個で文字列を囲むことで取り消し線を利用できます。</p>

<h3>
<span id="記述例-10" class="fragment"></span><a href="#%E8%A8%98%E8%BF%B0%E4%BE%8B-10"><i class="fa fa-link"></i></a>記述例</h3>

<div class="code-frame" data-lang="md"><div class="highlight"><pre>~~取り消し線~~
</pre></div></div>

<h3>
<span id="表示例-12" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B-12"><i class="fa fa-link"></i></a>表示例</h3>

<p><del>取り消し線</del></p>

<h2>
<span id="-gfmpre記法チルダ3" class="fragment"></span><a href="#-gfmpre%E8%A8%98%E6%B3%95%E3%83%81%E3%83%AB%E3%83%803"><i class="fa fa-link"></i></a><i></i> GFM:pre記法(チルダ×3)</h2>

<h3>
<span id="記述例-11" class="fragment"></span><a href="#%E8%A8%98%E8%BF%B0%E4%BE%8B-11"><i class="fa fa-link"></i></a>記述例</h3>

<div class="code-frame" data-lang="md"><div class="highlight"><pre>　~~~
　class Hoge
　  def hoge
　    print 'hoge'
　  end
　end
　~~~
</pre></div></div>

<h3>
<span id="表示例-13" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B-13"><i class="fa fa-link"></i></a>表示例</h3>

<div class="code-frame" data-lang="text"><div class="highlight"><pre>class Hoge
  def hoge
    print 'hoge'
  end
end
</pre></div></div>

<h2>
<span id="-gfmpre記法バッククォート3" class="fragment"></span><a href="#-gfmpre%E8%A8%98%E6%B3%95%E3%83%90%E3%83%83%E3%82%AF%E3%82%AF%E3%82%A9%E3%83%BC%E3%83%883"><i class="fa fa-link"></i></a><i></i> GFM:pre記法(バッククォート×3)</h2>

<h3>
<span id="記述例-12" class="fragment"></span><a href="#%E8%A8%98%E8%BF%B0%E4%BE%8B-12"><i class="fa fa-link"></i></a>記述例</h3>

<div class="code-frame" data-lang="md"><div class="highlight"><pre>　<span class="sb">```
　class Hoge
　  def hoge
　    print 'hoge'
　  end
　end
　```</span>
</pre></div></div>

<h3>
<span id="表示例-14" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B-14"><i class="fa fa-link"></i></a>表示例</h3>

<div class="code-frame" data-lang="text"><div class="highlight"><pre>class Hoge
  def hoge
    print 'hoge'
  end
end
</pre></div></div>

<h2>
<span id="-gfmpre記法シンタックスハイライト" class="fragment"></span><a href="#-gfmpre%E8%A8%98%E6%B3%95%E3%82%B7%E3%83%B3%E3%82%BF%E3%83%83%E3%82%AF%E3%82%B9%E3%83%8F%E3%82%A4%E3%83%A9%E3%82%A4%E3%83%88"><i class="fa fa-link"></i></a><i></i> GFM:pre記法(シンタックスハイライト)</h2>

<p>チルダ、もしくはバッククォート3つの後ろに対象シンタックスの言語名を記述します。</p>

<h3>
<span id="記述例-13" class="fragment"></span><a href="#%E8%A8%98%E8%BF%B0%E4%BE%8B-13"><i class="fa fa-link"></i></a>記述例</h3>

<div class="code-frame" data-lang="md"><div class="highlight"><pre>　~~~ruby
　class Hoge
　  def hoge
　    print 'hoge'
　  end
　end
　~~~
</pre></div></div>

<h3>
<span id="表示例-15" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B-15"><i class="fa fa-link"></i></a>表示例</h3>

<div class="code-frame" data-lang="ruby"><div class="highlight"><pre><span class="k">class</span> <span class="nc">Hoge</span>
  <span class="k">def</span> <span class="nf">hoge</span>
    <span class="nb">print</span> <span class="s1">'hoge'</span>
  <span class="k">end</span>
<span class="k">end</span>
</pre></div></div>

<h2>
<span id="-gfm表組み" class="fragment"></span><a href="#-gfm%E8%A1%A8%E7%B5%84%E3%81%BF"><i class="fa fa-link"></i></a><i></i> GFM:表組み</h2>

<h3>
<span id="記述例-14" class="fragment"></span><a href="#%E8%A8%98%E8%BF%B0%E4%BE%8B-14"><i class="fa fa-link"></i></a>記述例</h3>

<div class="code-frame" data-lang="md"><div class="highlight"><pre>|header1|header2|header3|
|:--|--:|:--:|
|align left|align right|align center|
|a|b|c|
</pre></div></div>

<h3>
<span id="表示例-16" class="fragment"></span><a href="#%E8%A1%A8%E7%A4%BA%E4%BE%8B-16"><i class="fa fa-link"></i></a>表示例</h3>

<table>
<thead>
<tr>
<th style="text-align: left">header1</th>
<th style="text-align: right">header2</th>
<th style="text-align: center">header3</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">align left</td>
<td style="text-align: right">align right</td>
<td style="text-align: center">align center</td>
</tr>
<tr>
<td style="text-align: left">a</td>
<td style="text-align: right">b</td>
<td style="text-align: center">c</td>
</tr>
</tbody>
</table>

<h2>
<span id="gfmページ内リンク" class="fragment"></span><a href="#gfm%E3%83%9A%E3%83%BC%E3%82%B8%E5%86%85%E3%83%AA%E3%83%B3%E3%82%AF"><i class="fa fa-link"></i></a>GFM:ページ内リンク</h2>

<p>GitHubのMarkdownを利用すると、見出し記法を利用した際に<br>
アンカーが自動的に作成されます。<br>
そのアンカーを利用したページ内リンクを簡単に作成できます。</p>

<div class="code-frame" data-lang="md"><div class="highlight"><pre><span class="gu">## &lt;i class="fa fa-cube" style="font-size:1em;"&gt;&lt;/i&gt; menu</span>
<span class="p">*</span> <span class="p">[</span><span class="nv">to header1</span><span class="p">](</span><span class="sx">#header1</span><span class="p">)</span>
<span class="p">*</span> <span class="p">[</span><span class="nv">to header2</span><span class="p">](</span><span class="sx">#header2</span><span class="p">)</span>

<span class="c">&lt;!-- some long code --&gt;</span>

<span class="p">[</span><span class="nv">return to menu</span><span class="p">](</span><span class="sx">#menu</span><span class="p">)</span>
<span class="gu">### header1</span>
<span class="gu">### header2</span>
</pre></div></div>

<p>少し省略してますが、こんなかんじのHTMLになります。</p>

<div class="code-frame" data-lang="html"><div class="highlight"><pre><span class="nt">&lt;h2&gt;&lt;a</span> <span class="na">name=</span><span class="s">"user-content-menu"</span> <span class="na">href=</span><span class="s">"#menu"</span><span class="nt">&gt;</span>menu<span class="nt">&lt;/a&gt;&lt;/h2&gt;</span>
<span class="nt">&lt;a</span> <span class="na">href=</span><span class="s">"#header1"</span><span class="nt">&gt;</span>to header1<span class="nt">&lt;/a&gt;</span>
<span class="nt">&lt;a</span> <span class="na">href=</span><span class="s">"#header2"</span><span class="nt">&gt;</span>to header2<span class="nt">&lt;/a&gt;</span>

<span class="c">&lt;!-- some long code --&gt;</span>

<span class="nt">&lt;a</span> <span class="na">href=</span><span class="s">"#menu"</span><span class="nt">&gt;</span>to menu<span class="nt">&lt;/a&gt;</span>
<span class="nt">&lt;h3&gt;&lt;a</span> <span class="na">name=</span><span class="s">"user-content-header1"</span> <span class="na">href=</span><span class="s">"#header1"</span><span class="nt">&gt;</span>header1<span class="nt">&lt;/a&gt;&lt;/h3&gt;</span>
<span class="nt">&lt;h3&gt;&lt;a</span> <span class="na">name=</span><span class="s">"user-content-header2"</span> <span class="na">href=</span><span class="s">"#header2"</span><span class="nt">&gt;</span>header2<span class="nt">&lt;/a&gt;&lt;/h3&gt;</span>
</pre></div></div>

<h2>
<span id="-参照" class="fragment"></span><a href="#-%E5%8F%82%E7%85%A7"><i class="fa fa-link"></i></a><i></i> 参照</h2>

<p><a href="http://qiita.com/Qiita/items/c686397e4a0f4f11683d" id="reference-fa7669daa8d49bfa4c69">QiitaでのMarkdownの使用について</a><br>
<a href="http://blog.qiita.com/post/77055935852/qiita-toc" rel="nofollow noopener" target="_blank">Qiitaの目次生成機能について</a></p>
</div></section>